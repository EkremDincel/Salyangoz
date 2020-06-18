from ply import yacc

class Parser():

    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module = self)
        
    def parse(self, text):
        return self.parser.parse(text, lexer = self.lexer.lexer)

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('left', 'EQ', 'NE', 'LT', 'GT')
        )

    start = "statements"

    def p_scope(self, p):
        "scope : '{' statements '}'"
        p[0] = ("scope", p[2])

    def p_empty_scope(self, p):
        "scope : '{' '}'"
        p[0] = ("scope", None)

    def p_statements(self, p):
        "statements : statements statement"
        p[0] = p[1] + (p[2],)

    def p_statements_last(self, p):
        "statements : statement"
        p[0] = p[1],

    def p_statement(self, p):
        """statement : scope
                     | var_assign
                     | compound_expr
                     | import_stmt"""
        p[0] = p[1]

    def p_import_stmt(self, p):
        """import_stmt : IMPORT names"""
        p[0] = ("use", p[2])

    def p_importall_stmt(self, p):
        """import_stmt : IMPORTALL names"""
        p[0] = ("useall", p[2])

    def p_names(self, p):
        "names : names ',' NAME"
        p[0] = (p[3],) + p[1]

    def p_names_last(self, p):
        "names : NAME"
        p[0] = p[1],

    def p_statement_pop(self, p):
        """statement : eval_expr"""
        p[0] = ("pop", p[1])

    def p_var_assign(self, p):
        """var_assign : NAME EQUAL eval_expr"""
        p[0] = ("assign", p[1], p[3])

    def p_args(self, p):
        "args : args ',' eval_expr"
        p[0] = (p[3],) + p[1]

    def p_args_last(self, p):
        "args : eval_expr"
        p[0] = p[1],

    def p_eval_expr_paren(self, p):
        "eval_expr : LPAREN eval_expr RPAREN"
        p[0] = p[2]
        
    def p_eval_expr(self, p):
        """eval_expr : var
                     | const
                     | func_call
                     | compare_expr"""
        p[0] = p[1]

    def p_eval_op_expr(self, p):
        """eval_expr : eval_expr TIMES eval_expr
                     | eval_expr DIVIDE eval_expr
                     | eval_expr PLUS eval_expr
                     | eval_expr MINUS eval_expr"""
        f, s = p[1], p[3]
        if f[0] == s[0] == "const":
            p[0] = ("const", str(operantor_dict[p[2]](literal_eval(f[1]), literal_eval(s[1]))))
        else:
            p[0] = ("op", p[2], s, f)

    def p_const(self, p):
        """const : NUMBER
                 | STRING
                 | FLOAT"""
        p[0] = ("const", p[1])

    def p_var(self, p):
        """var : NAME"""
        p[0] = ("var", p[1])

    def p_func_call(self, p):
        """func_call : eval_expr LPAREN RPAREN"""
        p[0] = ("call", p[1])

    def p_arg_func_call(self, p):
        """func_call : eval_expr LPAREN args RPAREN"""
        p[0] = ("argcall", p[1], p[3])

    def p_compound_expr(self, p):
        """compound_expr : if_stmt
                         | while_stmt"""
        p[0] = p[1]

    def p_if_stmt(self, p):
        """if_stmt : IF eval_expr THEN scope"""
        p[0] = ("ifstmt", p[2], p[4])
        
    def p_ifelse_stmt(self, p):
        """if_stmt : IF eval_expr THEN scope ELSE scope"""
        p[0] = ("ifelse", p[2], p[4], p[6])

    def p_while(self, p):
        """while_stmt : eval_expr WHILE scope"""
        p[0] = ("while", p[1], p[3])

    def p_compare(self, p):
        """compare_expr : eval_expr EQ eval_expr
                        | eval_expr NE eval_expr
                        | eval_expr GT eval_expr
                        | eval_expr LT eval_expr"""
        p[0] = ("cmp", p[2], p[3], p[1])

    def p_error(self, p):
        if p is None:
            raise SyntaxError(p)
        print(f"Illegal token {p.value!r} of type {p.type!r} at {p.lineno}:{p.lexpos}")

if __name__ == "__main__":
    from lexer import Lexer
    p = Parser(Lexer())
    kod = """

"""
    print(p.parse(kod))
