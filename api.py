from __future__ import annotations
from importlib import reload
import runpy
import os

def loadmodule(module_name: str, path: list[str]): # sys.modules işini hallet
    for directory in path:
        for dosya in os.listdir(directory):
            if dosya.endswith(".py") and dosya[:-3] == module_name:
                m = runpy.run_path(os.path.join(directory, dosya))
                return m["Salyangoz"]

