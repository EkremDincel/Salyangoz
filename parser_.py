from ply import yacc
from lexer import Lexer
from ast import literal_eval
import operator

operator_dict =  {"+": operator.add,
                  "-": operator.sub,
                  "/": operator.truediv,
                  "//": operator.floordiv,
                  "*": operator.mul,
                  "**": operator.pow,
                  "%": operator.mod,
                  #
                  "<": operator.lt,
                  ">": operator.gt,
                  "<=": operator.le,
                  ">=": operator.ge,
                  "==": operator.eq,
                  "!=": operator.ne,}


class Parser():
    tokens = Lexer.tokens

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.parser = yacc.yacc(module = self)

    def parse(self, text: str):
        return self.parser.parse(text, lexer = self.lexer.lexer))

    

    def p_error(self, p):
        if p is None:
            raise SyntaxError()
        raise SyntaxError(f"Illegal token {p.value!r} of type {p.type!r} at {p.lineno}:{p.lexpos}")

if __name__ == "__main__":
    from lexer import Lexer
    p = Parser(Lexer())
    kod = """
a=1
"""
    print(p.parse(kod))
