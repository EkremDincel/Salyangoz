from interpreter import Interpreter
from astcompiler import Compiler
from parser_ import Parser
from lexer import Lexer

kod = """
yaz(tür(1))
"""

Interpreter().execute_bytecode(Compiler().compile_ast(Parser(Lexer()).parse(kod)))
