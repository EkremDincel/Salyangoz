from sly import Lexer

class Lexer(Lexer):

    tokens = {
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
        "FLOORDIV", # //
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
        "NEWLINES",    # \n | \n\r
##        "COMMENT",    # #
        "DOT",        # .
        "COLON",      # :
##        "BLOCKCOMMENT" # <- -> # can nest in another block comment and multiline
        }

    @_(r'\d+\.\d+') # 1. and .1 are invalid
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    NAME = r"[\w_][\w0-9_]*"

    #keywords
    NAME["doğru"] = TRUE
    NAME["yanlış"] = FALSE
    NAME["eğer"] = IF
    NAME["ise"] = THEN
    NAME["değilse"] = ELSE
    NAME["iken"] = WHILE
    NAME["değil"] = NOT
    
    EQUAL = r"="

    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACE  = r'\{'
    RBRACE  = r'\}'
    LSQRB   = r'\['
    RSQRB   = r'\]'

    PLUS     = r'\+'
    MINUS    = r'-'
    TIMES    = r'\*'
    FLOORDIV = r'//'
    DIVIDE   = r'/'
    POWER    = r'\*\*'
    MODULO   = r'%'

    @_(r"<-")
    def ignore_blockcomment(self, t): # "<" (LT)'den önce olmak zorunda
        block_count = 1
        try:
            while block_count:
                self.index += 1
                if self.text[self.index] == "-": # ->
                    if self.text[self.index+1] == ">":
                        block_count -= 1
                        self.index += 1
                elif self.text[self.index] == "<": # <-
                    if self.text[self.index+1] == "-":
                        block_count += 1
                        self.index += 1
        except IndexError:
            pass # "<- kjadskajd (EOF)" gibi şeylerin mümkün olmasını istiyoruz
        self.index += 1 # while'a girilmediği için ilk self.index += 1 kısmı işe yaramıyor

    EQ = r"=="
    LE = r"<="
    GE = r">="
    LT = r"<"
    GT = r">"
    NE = r"!="

    COMMA     = r","
    SEMICOLON = r";"
    DOT       = r"\."
    COLON     = r":"

    ignore = " \t"
    ignore_comment = r"\#.*" # "." yeni satır karakterini almıyor    
    

##    literals = ""

    @_(r'''(".*?")|('.*?')''') # needs rework
    def STRING(self, t): 
        t.value = literal_eval(t.value)
        return t
    
    @_(r"\n+") # is this OKAY?
    def NEWLINES(self, t):
        self.lineno += len(t.value)
        return t

    def error(self, t):
        SyntaxError(f"Illegal character {t.value[0]!r} at {t.lineno}:{t.lexpos-self.lexer.lastlexpos}")
