from .language import Language, LangMap

# Force Import all language modules in this directory.
# Without this code, None of the language modules will be imported, thus not supported on cli.
from os import listdir
import importlib
for file in listdir(__file__.rstrip("__init__.py")):
    if file.endswith(".py") and file not in  ("__init__.py", "errors.py"):
        importlib.import_module(f"lang.{file[:-3]}")

__all__ = ("Language", "LangMap")
