from __future__ import annotations
import api

defaultbuiltins =  {#fonksiyonlar
                    "yaz": print,
                    "oku": input,
                    "aç": open,
                    "mutlak_değer": abs,
                    "sekizli": oct,
                    "onaltılı": hex,
                    "uzunluk": len,
                    #veri tipleri
                    "sayı": int,
                    "kesir": float,
                    "ikili": bool,
                    "yazı": str,
                    "liste": list,
                    "dizi": tuple,
                    "küme": set,
                    "donmuşküme": frozenset,
                    "sözlük": dict,
                    }


class Interpreter():

    def __init__(self, builtins: dict[str, object] = None):
        #initialize interpreter
        self.stack = []
        self.points = []
        self.scopes = []
        self.current_scope = None
        if builtins == None:
            self.builtins = defaultbuiltins.copy()
        #setup sys library
        lib_path = "lib" # daha sonra kütüphane yap
        sys_lib = "sistem"
        self.sys = api.loadmodule(sys_lib, (lib_path,)) 
        self.sys.modüller[sys_lib] = self.sys
        self.sys.dizinler.append(lib_path)

    def execute(bytecode: str, *, debug: bool = True, ):
        
        if debug:
            ...



    def run(file, *, debug: bool = True, ):
        if debug:
            ...
