#!/usr/bin/env python3
# coding: utf-8

import abc
import logging
import os
import re
import weakref

from volkanic import utils
from volkanic.compat import cached_property, abstract_property

_logger = logging.getLogger(__name__)


class SingletonMeta(type):
    registered_instances = {}

    def __call__(cls, *args, **kwargs):
        try:
            return cls.registered_instances[cls]
        except KeyError:
            obj = super().__call__(*args, **kwargs)
            return cls.registered_instances.setdefault(cls, obj)


class WeakSingletonMeta(SingletonMeta):
    registered_instances = weakref.WeakValueDictionary()


class Singleton(metaclass=SingletonMeta):
    pass


class WeakSingleton(metaclass=WeakSingletonMeta):
    pass


class _GIMeta(SingletonMeta):
    def __new__(mcs, name, bases, attrs):
        pn = attrs.get('package_name')
        if pn is None:
            msg = '{}.package_name is missing'.format(name)
            raise ValueError(msg)
        if not isinstance(pn, str):
            msg = '{}.package_name is of wrong type'.format(name)
            raise TypeError(msg)
        if not re.match(r'\w[\w.]*\w', pn):
            msg = 'invalid {}.package_name: "{}"'.format(name, pn)
            raise ValueError(msg)
        return super().__new__(mcs, name, bases, attrs)


class _PackageNameDerivant:
    __slots__ = ['_sep']

    def __init__(self, sep):
        self._sep = sep

    def __get__(self, _, owner):
        return owner.package_name.replace('.', self._sep)


class GlobalInterface(metaclass=_GIMeta):
    # python dot-deliminated path, [a-z.]+
    package_name = 'volkanic'

    # for path and url
    # dot '.' in package_name replaced by hyphen '-'
    project_name = _PackageNameDerivant('-')

    # for symbols in code
    # dot '.' in package_name replaced by underscore '_'
    identifier = _PackageNameDerivant('_')

    _options = {
        # for project dir locating (under_project_dir())
        'project_source_depth': 0,
        # for config file locating (_get_conf_paths())
        'confpath_filename': 'config.json5',
        # for config file locating (_get_conf_paths())
        'confpath_dirname_sep': '-',
    }

    # default config and log format
    default_config = {
        '_jinja2_env': {},
    }
    default_logfmt = \
        '%(asctime)s %(levelname)s [%(process)s,%(thread)s] %(name)s %(message)s'

    @classmethod
    def _fmt_envvar_name(cls, name):
        return '{}_{}'.format(cls.identifier, name).upper()

    @classmethod
    def _get_option(cls, key: str):
        for c in cls.mro():
            options = c.__dict__.get('_options')
            try:
                return options[key]
            except (KeyError, TypeError):
                pass

    @classmethod
    def _fmt_name(cls, sep='-'):
        return cls.package_name.replace('.', sep)

    @classmethod
    def _get_conf_paths(cls):
        """
        Make sure this method can be called without arguments.
        Override this method in your subclasses for your specific project.
        """
        envvar_name = cls._fmt_envvar_name('confpath')
        fn = cls._get_option('confpath_filename')
        pn = cls._fmt_name(cls._get_option('confpath_dirname_sep'))
        return [
            os.environ.get(envvar_name),
            cls.under_project_dir(fn),
            utils.under_home_dir('.{}/{}'.format(pn, fn)),
            '/etc/{}/{}'.format(pn, fn),
            '/{}/{}'.format(pn, fn),
        ]

    # _get_conf_search_paths is deprecated
    # _get_conf_search_paths will be remove at ver 0.5.0
    _get_conf_search_paths = _get_conf_paths

    @classmethod
    def _locate_conf(cls):
        """
        Returns: (str) absolute path to config file
        """
        # _get_conf_search_paths is deprecated
        # _get_conf_search_paths will be remove at ver 0.5.0
        func = getattr(cls, '_get_conf_search_paths', None)
        if func is None:
            func = cls._get_conf_paths
        paths = func()
        for path in paths:
            if not path:
                continue
            if os.path.exists(path):
                return os.path.abspath(path)

    @staticmethod
    def _parse_conf(path: str):
        return utils.load_json5_file(path)

    @staticmethod
    def _check_conf(config: dict):
        return config

    @cached_property
    def conf(self) -> dict:
        path = self._locate_conf()
        cn = self.__class__.__name__
        if path:
            config = self._parse_conf(path)
            utils.printerr('{}.conf, path'.format(cn), path)
        else:
            config = {}
            utils.printerr('{}.conf, hard-coded'.format(cn))
        config = utils.merge_dicts(self.default_config, config)
        return self._check_conf(config)

    @staticmethod
    def under_home_dir(*paths):
        return utils.under_home_dir(*paths)

    @classmethod
    def under_package_dir(cls, *paths) -> str:
        return utils.under_package_dir(cls.package_name, *paths)

    @classmethod
    def under_project_dir(cls, *paths):
        pkg_dir = cls.under_package_dir()
        if re.search(r'[/\\](site|dist)-packages[/\\]', pkg_dir):
            return
        n = cls._get_option('project_source_depth')
        n += len(cls.package_name.split('.'))
        paths = ['..'] * n + list(paths)
        return utils.abs_path_join(pkg_dir, *paths)

    # deprecated
    # this method will be removed at ver 0.5.0
    @cached_property
    def jinja2_env(self):
        # noinspection PyPackageRequirements
        from jinja2 import Environment, PackageLoader, select_autoescape
        return Environment(
            loader=PackageLoader(self.package_name, 'templates'),
            autoescape=select_autoescape(['html', 'xml']),
            **self.conf.get('_jinja2_env', {})
        )

    @classmethod
    def setup_logging(cls, level=None, fmt=None):
        if not level:
            envvar_name = cls._fmt_envvar_name('loglevel')
            level = os.environ.get(envvar_name, 'DEBUG')
        fmt = fmt or cls.default_logfmt
        logging.basicConfig(level=level, format=fmt)


# deprecated
# this class will be removed at ver 0.4.0
class GIMixinDirs:
    @abstract_property
    def conf(self) -> dict:
        return NotImplemented

    @abc.abstractmethod
    def under_project_dir(self, *paths) -> str:
        return NotImplemented

    def _under_data_dir(self, conf_key, *paths, mkdirs=False) -> str:
        dirpath = self.conf[conf_key]
        if not mkdirs:
            return utils.abs_path_join(dirpath, *paths)
        return utils.abs_path_join_and_mkdirs(dirpath, *paths)

    def under_data_dir(self, *paths, mkdirs=False) -> str:
        return self._under_data_dir('data_dir', *paths, mkdirs=mkdirs)

    def _under_resources_dir(self, conf_key, default, *paths) -> str:
        dirpath = self.conf.get(conf_key)
        if not dirpath:
            dirpath = self.under_project_dir(default)
        if not dirpath or not os.path.isdir(dirpath):
            raise NotADirectoryError(dirpath)
        return utils.abs_path_join(dirpath, *paths)

    def under_resources_dir(self, *paths) -> str:
        f = self._under_resources_dir
        return f('resources_dir', 'resources', *paths)

    def under_temp_dir(self, ext=''):
        name = os.urandom(17).hex() + ext
        return self.under_data_dir('tmp', name, mkdirs=True)

    # both will be removed
    get_temp_path = under_temp_dir
    under_temp_path = under_temp_dir
