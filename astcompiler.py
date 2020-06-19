operands = {"+":"add", "-":"sub", "/":"div", "*":"mul"}

__all__ = ["Compiler"]

nodes = {}
def node(f):
    nodes[f.__name__] = f
    return f

class Compiler():
    line_number = 0 # __init__

    __all__ = ["compile_ast"]

    def walk_node(self, ast):
        node, *elements = ast
        s = nodes[node](self, *elements)
        return s

    compile_ast = walk_node # main funtion
    

    @node
    def scope(self, e):
        self.line_number += 1
        if not e: return ""
        s = "scope 1\n"
        for i in e:
            s += self.walk_node(i)
        self.line_number += 1
        return s + "scope -1\n"

    @node
    def pop(self, e):
        r = self.walk_node(e) + "pop\n"
        self.line_number += 1
        return r

    @node
    def use(self, e):
        s = ""
        for i in e:
            s += "use " + i + "\n"
            self.line_number += 1
        return s

    @node
    def useall(self, e):
        s = ""
        for i in e:
            s += "useall " + i + "\n"
            self.line_number += 1
        return s

    @node
    def assign(self, name, expr):
        r = self.walk_node(expr) + "storename " + name + "\n"
        self.line_number += 1
        return r

    @node
    def op(self, operand, a, b):
        r = self.walk_node(a) + self.walk_node(b) + "op " + operands[operand] + "\n"
        self.line_number += 1
        return r

    @node
    def const(self, c):
        self.line_number += 1
        return "loadconst " + c + "\n"

    @node
    def var(self, n):
        self.line_number += 1
        return "loadname " + n + "\n"

    @node
    def call(self, expr):
        r = self.walk_node(expr) + "call 0\n"
        self.line_number += 1
        return r

    @node
    def argcall(self, expr, args):
        s = ""
        for i in args:
            s += self.walk_node(i)
        r = s + self.walk_node(expr) + "call " + str(len(args)) + "\n"
        self.line_number += 1
        return r

    @node
    def cmp(self, t, l, r):
        r = self.walk_node(l) + self.walk_node(r) + "cmp " + t + "\n"
        self.line_number += 1
        return r

    @node
    def ifstmt(self, eval_expr, scope):
        condition = self.walk_node(eval_expr)
        self.line_number += 1
        s = self.walk_node(scope)
        return condition + "jumpnif " + str(self.line_number) + "\n" + s

    @node
    def ifelse(self, eval_expr, if_scope, else_scope):
        condition = self.walk_node(eval_expr)
        self.self.line_number += 1
        if_s = self.walk_node(if_scope)
        self.line_number += 1
        tail_of_if = self.self.line_number
        else_s = self.walk_node(else_scope)
        jump_to_else = "jumpnif " + str(tail_of_if) + "\n"
        pass_else = "jump " + str(self.self.line_number) + "\n"
        return condition + jump_to_else + if_s + pass_else + else_s










