from sty import fg, bg, ef, rs
import os
from types import SimpleNamespace

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add custom colors:

from sty import Style, RgbFg

fg.orange = Style(RgbFg(255, 150, 50))

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(foo, bar, baz, qux, qui, buf, sep='\n')

    

class Salyangoz():
    def __init__(self, interpreter):
        self.__sys = interpreter.sistem

    def yaz(self, yazı, stil):
        ön = son = ""
        if t := stil.get("renk", None):
            ön += fg(*t)
            son += fg.rs
            
        if t := stil.get("arkaplan", None):
            ön += bg(*t)
            son += bg.rs
            
        self.__sys.standart_çıkış.write(ön + yazı + son)

    #temizle
    if os.name == "nt":
        os.system("color")
        def temizle(self):
            os.system("cls")
    elif os.name == "posix":
        def temizle(self):
            os.system("clear")

    def aynı_satıra_yaz(self, yazı):
        self.__sys.standart_çıkış.write("\r" + yazı)
