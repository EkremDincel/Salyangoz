from interpreter import Interpreter
from astcompiler import Compiler
from parser_ import Parser
from lexer import Lexer

kod = """
a = (1,2, 3, 4)

"""

##bytecode = Compiler().compile_ast(Parser(Lexer()).parse(kod))

##Interpreter().execute_bytecode(bytecode)

print(Parser(Lexer()).parse(kod))
