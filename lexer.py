from ply import lex

class Lexer():

    def __init__(self):
        self.lexer = lex.lex(module = self)

    tokens = [
        #vars
        "NAME",
        #assign
        "EQUAL",
        #parenthesis
        "LPAREN",
        "RPAREN",
        #keywords        
        "IF",
        "THEN",
        "ELSE",
        "WHILE",
        "IMPORT",
        "IMPORTALL",
        #consts
        "STRING",
        "NUMBER",
        "FLOAT",
        #literals
        "TRUE",
        "FALSE",
        #operators
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "POWER",
        #compare
        "EQ",
        "LT",
        "GT",
        "NE",
        ]

    t_NAME = r"\w[\w0-9_]*"
    t_EQUAL = r"="

    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_POWER   = r'\*\*'

    t_EQ = r"=="
    t_LT = r"<"
    t_GT = r">"
    t_NE = r"!="

    t_ignore = " \t"

    literals = ",{};"

    def t_TRUE(self, t): r'doğru'; return t
    def t_FALSE(self, t): r'yanlış'; return t

    def t_IF(self, t): r'eğer'; return t
    def t_THEN(self, t): r'ise'; return t
    def t_ELSE(self, t): r'değilse'; return t

    def t_WHILE(self, t): r'iken'; return t

    def t_IMPORT(self, t): r'kullan:'; return t
    def t_IMPORTALL(self, t): r'aktar:'; return t

    def t_FLOAT(self, t):
        r'\d+\.\d*|\d+\.\d*'
    ##    t.value = float(t.value)
        return t

    def t_NUMBER(self, t):
        r'\d+|\d+'
    ##    t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r'''(".*?")|('.*?')'''
    ##    t.value = literal_eval(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        SyntaxError(f"Illegal character {t.value[0]!r} at {t.lineno}:{t.lexpos}")
