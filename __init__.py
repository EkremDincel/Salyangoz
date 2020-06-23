from interpreter import Interpreter
from astcompiler import Compiler
from parser_ import Parser
from lexer import Lexer

kod = """
a=oku()
yaz(aç)
"""

Interpreter().execute_bytecode(Compiler().compile_ast(Parser(Lexer()).parse(kod)))
