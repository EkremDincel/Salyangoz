from ast import literal_eval
import api
import sys
##import operator

commands = {}

def command(f):
    commands[f.__name__] = f
    return f

class ByteCodeInterpreter():

    @command
    def loadname(self, name):
        try:
            self.stack.append(self.current_scope[name])
        except KeyError:
            try:
                self.stack.append(self.scopes[0][name]) # globals
            except KeyError:
                self.stack.append(self.builtins[name])

    @command
    def storename(self, name):
        self.current_scope[name] = self.stack.pop()

    @command
    def loadconst(self, const):
        self.stack.append(literal_eval(const))

    @command
    def call(self, n):
        self.stack.append(self.stack.pop()(*(self.stack.pop() for i in range(int(n)))))

    @command
    def cmp(self, a):
        if a == "==":
            s = self.stack.pop() == self.stack.pop()
        elif a == ">":
            s = self.stack.pop() > self.stack.pop()
        elif a == "<":
            s = self.stack.pop() < self.stack.pop()
        elif a == "!=":
            s = self.stack.pop() != self.stack.pop()
        self.stack.append(s)

    @command
    def op(self, a):
        if a == "add":
            s = self.stack.pop() + self.stack.pop()
        elif a == "sub":
            s = self.stack.pop() - self.stack.pop()
        elif a == "mul":
            s = self.stack.pop() * self.stack.pop()
        elif a == "div":
            s = self.stack.pop() / self.stack.pop()
        self.stack.append(s)

    @command
    def scope(self, n):
        n = int(n)
        if n < 0:
            for i in range(-n):
                self.scopes.pop()
            try:
                self.current_scope = self.scopes[-1]
            except IndexError:
                self.current_scope = None
        else:
            for i in range(n):
                self.scopes.append({})
            self.current_scope = self.scopes[-1]

    @command
    def pop(self, ):
        self.stack.pop()

    @command
    def use(self, module_name):
        try:
            m = self.sistem.modüller[module_name]
        except:
            m = api.loadmodule(module_name)
            self.sistem.modüller[module_name] = m
        self.current_scope[module_name] = m
            

    @command
    def useall(self, module_name):
        try:
            m = self.sistem.modüller[module_name]
        except:
            m = api.loadmodule(module_name)
            self.sistem.modüller[module_name] = m
        self.current_scope.update(m)

    @command
    def jump(self, n):
        self.points[-1] = int(n) -1

    @command
    def jumpif(self, n):
        e = self.stack.pop()
        assert type(e) == bool
        if e:
            self.points[-1] = int(n) -1

    @command
    def jumpnif(self, n):
        e = self.stack.pop()
        assert type(e) == bool
        if not e:
            self.points[-1] = int(n) -1
    ##########


    def exec_line(self, line):
        try:
            c, f = line
        except ValueError:
            c = line[0]
            commands[c](self)
            return
        commands[c](self, f)

    def exec_code(self, code):
        code = optimize_code(code)
        while True:
            try:
                c = code[self.points[-1]]
            except IndexError:
                input("[Program Finished]")
                break
            self.exec_line(c)
            self.points[-1] += 1



def optimize_code(code):
    code = code.split("\n")
    r = []
    for line in code:
        s = tuple(line.split(" ", 1))
        if s[0]:
            r.append(s)
    return r




