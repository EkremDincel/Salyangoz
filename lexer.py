from ply import lex

class Lexer():

    def __init__(self):
        self.lexer = lex.lex(module = self)
        self.lexer.lastlexpos = 0

    tokens = [
        #vars
        "NAME",
        #assign
        "EQUAL",  # =
        #parenthesis
        "LPAREN", # (
        "RPAREN", # )
        "LBRACE", # {
        "RBRACE", # }
        "LSQRB",  # [
        "RSQRB",  # ]
        #keywords        
        "IF",
        "THEN",
        "ELSE",
        "WHILE",
        "AND",
        "OR",
        "NOT",
        #consts
        "STRING",
        "NUMBER",
        "FLOAT",
        #literals
        "TRUE",
        "FALSE",
        #operators
        "POWER",      # **
        "MODULO",     # %
        "INTEGERDIV", # //
        "PLUS",       # +
        "MINUS",      # -
        "TIMES",      # *
        "DIVIDE",     # /
        #compare
        "EQ",   # ==
        "NE",   # !=
        "LE",   # <=
        "GE",   # >=
        "LT",   # <
        "GT",   # >
        #other
        "COMMA",      # ,
        "SEMICOLON",  # ;
        "NEWLINE",    # \n | \n\r
        "COMMENT",    # #
        # ekle : multiline comments
        ]

    t_NAME = r"\w[\w0-9_]*"
    t_EQUAL = r"="

    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_LBRACE  = r'\['
    t_RBRACE  = r'\]'
    t_LSQRB   = r'\{'
    t_RSQRB   = r'\}'

    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_INTEGERDIV = r'//'
    t_DIVIDE  = r'/'
    t_POWER   = r'\*\*'
    t_MODULO  = r'%'
    
    t_EQ = r"=="
    t_LE = r"<="
    t_GE = r">="
    t_LT = r"<"
    t_GT = r">"
    t_NE = r"!="

    t_COMMA     = r","
    t_SEMICOLON = r";"

    t_ignore = " \t"

##    literals = ""

    def t_TRUE(self, t): r'doğru'; return t
    def t_FALSE(self, t): r'yanlış'; return t

    def t_IF(self, t): r'eğer'; return t
    def t_THEN(self, t): r'ise'; return t
    def t_ELSE(self, t): r'değilse'; return t

    def t_WHILE(self, t): r'iken tekrarla'; return t

    def t_FLOAT(self, t):
        r'\d+\.\d+' # 1. and .1 are invalid
        t.value = float(t.value)
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING(self, t): # needs rework
        r'''(".*?")|('.*?')'''
        t.value = literal_eval(t.value)
        return t

    def t_NEWLINE(self, t):
        r"(\n\r|\n|\r)+" # is this OKAY?
        if t.value.startswith("\n\r"):
            t.lexer.lineno += len(t.value) / 2
        else:
            t.lexer.lineno += len(t.value)
        self.lexer.lastlexpos = t.lexer.lexpos
        return t

    def t_error(self, t):
        SyntaxError(f"Illegal character {t.value[0]!r} at {t.lineno}:{t.lexpos-self.lexer.lastlexpos}")
