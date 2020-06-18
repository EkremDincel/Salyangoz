from __future__ import annotations

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

    def __init__(self, builtins: dict[str, object] = defaultbuiltins):
        #initialize interpreter
        self.stack = []
        self.points = []
        self.modules = {}
        self.scopes = []
        self.current_scope = None
        self.builtins = builtins

    def execute(bytecode: str, *, debug: bool = True, ):
        if debug:
            ...



    def run(file, *, debug: bool = True, ):
        if debug:
            ...
