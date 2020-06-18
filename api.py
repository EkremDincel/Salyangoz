from importlib import reload
import runpy
import os

def loadmodule(module_name, path): # sys.modules işini hallet
    for directory in path:
        for dosya in os.listdir(directory):
            if dosya.endswith(".py") and dosya[:-3] == module_name:
                m = runpy.run_path(os.path.join(directory, dosya))
                return m["Salyangoz"]

