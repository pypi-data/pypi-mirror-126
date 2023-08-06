import importlib
import sys
from types import ModuleType
from typing import Dict, List, Union

from ..config import Core
from ..utils.classproperty import classproperty
from ..utils.importing import import_module, module_importable, module_imported
from ..utils.log import logger


class Extension:
    """
    Extension descriptor

    :param module: main extension module
    :param reqs: list of extension dependencies
    :param force: if True, disable lazy loading for this extension
    :param validator: boolean predicate which should evaluate to True for this extension to be loaded
    """

    def __init__(self, module, reqs: List[str], force=True, validator=None):
        self.force = force
        self.reqs = reqs
        self.module = module
        self.validator = validator

    def __str__(self):
        return f'<Extension {self.module}>'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.module == other.module

    def __hash__(self):
        return hash(self.module)


class ExtensionDict(dict):
    """
    :class:`_Extension` container
    """

    def __init__(self, *extensions: Extension):
        super().__init__()
        for e in extensions:
            self[e.module] = e


def __tensorflow_major_version():
    import tensorflow as tf
    return tf.__version__.split('.')[0]


is_tf_v1, is_tf_v2 = lambda: __tensorflow_major_version() == '1', lambda: __tensorflow_major_version() == '2'


class ExtensionLoader:
    """
    Class that tracks and loads extensions.

    """
    builtin_extensions: Dict[str, Extension] = ExtensionDict(
        Extension('algolink.ext.numpy', ['numpy'], False),
        Extension('algolink.ext.pandas', ['pandas'], False),
        Extension('algolink.ext.sklearn', ['sklearn'], False),
        Extension('algolink.ext.tensorflow', ['tensorflow'], False, is_tf_v1),
        Extension('algolink.ext.tensorflow_v2', ['tensorflow'], False, is_tf_v2),
        Extension('algolink.ext.torch', ['torch'], False),
        Extension('algolink.ext.catboost', ['catboost'], False),
        Extension('algolink.ext.aiohttp', ['aiohttp', 'aiohttp_swagger']),
        Extension('algolink.ext.flask', ['flask', 'flasgger'], False),
        Extension('algolink.ext.sqlalchemy', ['sqlalchemy']),
        Extension('algolink.ext.s3', ['boto3']),
        Extension('algolink.ext.imageio', ['imageio']),
        Extension('algolink.ext.lightgbm', ['lightgbm'], False),
        Extension('algolink.ext.xgboost', ['xgboost'], False),
        Extension('algolink.ext.docker', ['docker'], False)
    )

    _loaded_extensions: Dict[Extension, ModuleType] = {}

    @classproperty
    def loaded_extensions(cls) -> Dict[Extension, ModuleType]:
        """
        :return: List of loaded extensions
        """
        return cls._loaded_extensions

    @classmethod
    def _setup_import_hook(cls, extensions: List[Extension]):
        """
        Add import hook to sys.meta_path that will load extensions when their dependencies are imported

        :param extensions: list of :class:`.Extension`
        """
        if len(extensions) == 0:
            return

        existing = [h for h in sys.meta_path if isinstance(h, _ImportLoadExtInterceptor)]
        if len(existing) > 0:
            hook = existing[0]
            hook.module_to_extension.update({req: e for e in extensions for req in e.reqs})
        else:
            hook = _ImportLoadExtInterceptor(
                module_to_extension={req: e for e in extensions for req in e.reqs}
            )
            sys.meta_path.insert(0, hook)

    @classmethod
    def load_all(cls, try_lazy=True):
        """
        Load all (builtin and additional) extensions

        :param try_lazy: if `False`, use force load for all builtin extensions
        """
        for_hook = []
        for ext in cls.builtin_extensions.values():
            if not try_lazy or hasattr(sys, 'frozen') or ext.force:
                if all(module_importable(r) for r in ext.reqs):
                    cls.load(ext)
            else:
                if all(module_imported(r) for r in ext.reqs):
                    cls.load(ext)
                else:
                    for_hook.append(ext)

        cls._setup_import_hook(for_hook)

        for mod in Core.ADDITIONAL_EXTENSIONS:
            cls.load(mod)

    @classmethod
    def load(cls, extension: Union[str, Extension]):
        """
        Load single extension

        :param extension: str of :class:`.Extension` instance to load
        """
        if isinstance(extension, str):
            extension = Extension(extension, [], force=True)
        if extension not in cls._loaded_extensions and not module_imported(extension.module) and \
                (extension.validator is None or extension.validator()):
            logger.debug('Importing extension module %s', extension.module)
            cls._loaded_extensions[extension] = import_module(extension.module)


class _ImportLoadExtRegisterer(importlib.abc.PathEntryFinder):
    """A hook that registers all modules that are being imported"""

    def __init__(self):
        self.imported = []

    def find_module(self, fullname, path=None):
        self.imported.append(fullname)
        return None


class _ImportLoadExtInterceptor(importlib.abc.Loader, importlib.abc.PathEntryFinder):
    """
    Import hook implementation to load extensions on dependency import

    :param module_to_extension: dict requirement -> :class:`.Extension`
    """

    def __init__(self, module_to_extension: Dict[str, Extension]):
        self.module_to_extension = module_to_extension

    def find_module(self, fullname, path=None):
        # hijack importing machinery
        return self

    def load_module(self, fullname):
        # change this hook to registering hook
        reg = _ImportLoadExtRegisterer()
        sys.meta_path = [reg] + [x for x in sys.meta_path if x is not self]
        try:
            # fallback to ordinary importing
            module = importlib.import_module(fullname)
        finally:
            # put this hook back
            sys.meta_path = [self] + [x for x in sys.meta_path if x is not reg]

        # check all that was imported and import all extensions that are ready
        for imported in reg.imported:
            if not module_imported(imported):
                continue
            extension = self.module_to_extension.get(imported)
            if extension is None:
                continue

            if all(module_imported(m) for m in extension.reqs):
                ExtensionLoader.load(extension)

        return module


def load_extensions(*exts: str):
    """
    Load extensions

    :param exts: list of extension main modules
    """
    for ext in exts:
        ExtensionLoader.load(ext)
