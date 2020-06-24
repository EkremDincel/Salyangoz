from interpreter import Interpreter
from astcompiler import Compiler
from parser_ import Parser
from lexer import Lexer

kod = """
isim = oku("Adın ne? > ")
yaz("Merhaba", isim + "!")
"""

bytecode = Compiler().compile_ast(Parser(Lexer()).parse(kod))

Interpreter().execute_bytecode(bytecode)

print(bytecode)
