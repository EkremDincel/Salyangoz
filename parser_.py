from sly import Parser
from lexer import Lexer
from enums import Nodes
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


class Parser(Parser):
    debugfile = "debug.txt"
    tokens = Lexer.tokens

    precedence = (
       ('left', PLUS, MINUS),
       ('left', TIMES, DIVIDE, FLOORDIV, MODULO),
       ('left', POWER),
       ('left', DOT)
    )
    
    start = "statements"

    @_("{ NEWLINES } { statement seperator }")
    def statements(self, p):
##        return p[1] + tuple(i[1] for i in p[2])
        return p.statement

    @_("SEMICOLON { NEWLINES }")
    @_("NEWLINES { NEWLINES }")
    def seperator(self, p):
        return

    @_("eval_expr")
    def statement(self, p):
        return (Nodes.POPLAST, p[0])

    @_("assign")
    def statement(self, p):
        return p[0]

    @_("var")
    def eval_expr(self, p):
        return p[0]

    @_("NAME EQUAL eval_expr")
    def assign(self, p):
        return (Nodes.STORENAME, p[0], p[2])

    @_("eval_expr DOT NAME EQUAL eval_expr")
    def assign(self, p):
        return (Nodes.STOREATTR, p[0], p[2], p[4])

    @_("tuple_literal")
    @_("set_literal")
    @_("list_literal")
    def literal(self, p):
        return p[0]

    @_("const")
    @_("literal")
    @_("func_call")
    def eval_expr(self, p):
        return p[0]

    @_("LPAREN eval_expr RPAREN")
    def eval_expr(self, p):
        return p[1]

    @_("NUMBER")
    @_("FLOAT")
    @_("STRING")
    def const(self, p):
        return (Nodes.LOADCONST, p[0])
    
    @_("eval_expr { COMMA eval_expr }")
    def arglist(self, p): #??
        return (p[0],) + tuple(p.eval_expr1)

    @_("eval_expr LPAREN arglist RPAREN ")
    def func_call(self, p):
        return (Nodes.CALLFUNC, p[0], p[2])

    @_("eval_expr LPAREN RPAREN")
    def func_call(self, p):
        return (Nodes.CALLFUNC, p[0], ())

    @_("LPAREN eval_expr COMMA RPAREN")
    def tuple_literal(self, p):
        return (Nodes.BUILDTUPLE, (p[1],))

    @_("LPAREN arglist RPAREN")
    def tuple_literal(self, p):
        return (Nodes.BUILDTUPLE, p[1])

    @_("LBRACE arglist RBRACE")
    def set_literal(self, p):
        return (Nodes.BUILDSET, p[1])

    @_("LSQRB arglist RSQRB")
    def list_literal(self, p):
        return (Nodes.BUILDLIST, p[1])

    @_("eval_expr PLUS eval_expr")
    @_("eval_expr MINUS eval_expr")
    @_("eval_expr TIMES eval_expr")
    @_("eval_expr DIVIDE eval_expr")
    @_("eval_expr FLOORDIV eval_expr")
    @_("eval_expr POWER eval_expr")
    @_("eval_expr MODULO eval_expr")
    def eval_expr(self, p):
        if p[0][0] == p[2][0] == Nodes.LOADCONST:
            return (Nodes.LOADCONST, operator_dict[p[1]](p[0][1], p[2][1]))
        return (Nodes.OP, p[1], p[0], p[2])

    @_("eval_expr EQ eval_expr")
    @_("eval_expr NE eval_expr")
    @_("eval_expr LE eval_expr")
    @_("eval_expr GE eval_expr")
    @_("eval_expr LT eval_expr")
    @_("eval_expr GT eval_expr")
    def eval_expr(self, p):
        if p[0][0] == p[2][0] == Nodes.LOADCONST:
            return (Nodes.LOADCONST, operator_dict[p[1]](p[0][1], p[2][1]))
        return (Nodes.CMP, p[1], p[0], p[2])

    @_("eval_expr DOT NAME")
    def var(self, p):
        return (Nodes.LOADATTR, p[0], p[2])

    @_("NAME")
    def var(self, p):
        return (Nodes.LOADNAME, p[0])
        
    def error(self, p):
        print(self.statestack, self.symstack)
        if p is None:
            raise SyntaxError()
        raise SyntaxError(f"Illegal token {p.value!r} of type {p.type!r} at {p.lineno}:{p.index}")

if __name__ == "__main__":
    from lexer import Lexer
    p = Parser()
    p.tokens = Lexer.tokens
    kod = """
a<2<3;"""
    ast = p.parse(Lexer().tokenize(kod))
    print(ast)
