from __future__ import annotations
import api
from bcinterpreter import ByteCodeInterpreter

defaultbuiltins =  {#fonksiyonlar
                    "yaz": print, # hallet
                    "oku": input,
                    "aç": open,
                    "mutlak_değer": abs,
                    "sekizli": oct,
                    "onaltılı": hex,
                    "uzunluk": len,
                    "ikili": bin,
                    "tür": type,
                    #veri tipleri
                    "sayı": int,
                    "kesir": float,
                    "mantıksal": bool,
                    "yazı": str,
                    "liste": list,
                    "dizi": tuple,
                    "küme": set,
                    "donmuşküme": frozenset,
                    "sözlük": dict,
                    }


class Interpreter(ByteCodeInterpreter):

    __all__ = ("execute_bytecode", "execute", "run")

    def __init__(self, builtins: dict[str, object] = None):
        #initialize interpreter
        self.stack = []
        self.points = [0]
        self.scopes = []
        self.current_scope = None
        if builtins == None:
            self.builtins = defaultbuiltins.copy()

        #setup sys library
        lib_path = "lib" # daha sonra kütüphane yap
        sys_lib = "sistem"
        self.sistem = api.loadmodule(sys_lib, (lib_path,), self) 
        self.sistem.modüller[sys_lib] = self.sistem
        self.sistem.dizinler.append(lib_path)

        #debug
        debug = 1
        if debug:
            debug_scopes = lambda: print(self.scopes)
            debug_stack = lambda: print(self.stack)
            debug_module = lambda: print(self.sistem.modüller)
            debug_points = lambda: print(self.points)

            self.builtins["scopes"] = debug_scopes
            self.builtins["stack"] = debug_stack
            self.builtins["modules"] = debug_module
            self.builtins["points"] = debug_points
        

    def execute_bytecode(self, bytecode: str, *, debug: bool = True, ):

        self.exec_code(bytecode)

    def execute(): # direkt kod
        ...

    def run(self, file, *, debug: bool = True, ):
        if debug:
            ...
