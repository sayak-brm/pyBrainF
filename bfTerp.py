##   Copyright 2016 Sayak Brahmachari
##
##   Licensed under the Apache License, Version 2.0 (the "License");
##   you may not use this file except in compliance with the License.
##   You may obtain a copy of the License at
##
##       http://www.apache.org/licenses/LICENSE-2.0
##
##   Unless required by applicable law or agreed to in writing, software
##   distributed under the License is distributed on an "AS IS" BASIS,
##   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##   See the License for the specific language governing permissions and
##   limitations under the License.

class Lexer:
    def __init__(self, code):
        self.code = code
        self.i = 0
    def nextChar(self):
        if self.i >= len(self.code):
            return ''
        self.i+=1
        return self.code[self.i-1]
    def peekChar(self):
        if self.i >= len(self.code):
            return ''
        return self.code[self.i]
    def nextCharsTill(self, end):
        ''' Returns following characters till given character. '''
        if self.i >= len(self.code):
            return ''
        i2 = self.i
        while self.code[i2] is not end:
            i2 += 1
            if i2 >= len(self.code):
                raise IndexError('string index out of range.')
        chars = self.code[self.i:i2]
        i2 += 1
        self.i = i2
        return chars

class Terp:
    def __init__(self):
        self.stack = [0]*1000
        self.i=0
    def run(self, code):
        self.lexer = Lexer(code)
        self.interpret(self.lexer)
        print()
    def interpret(self, lexer):
        while lexer.peekChar():
            cmd = lexer.nextChar()
            if cmd == '>': self.f1()
            elif cmd == '<': self.f2()
            elif cmd == '+': self.f3()
            elif cmd == '-': self.f4()
            elif cmd == '.': self.f5()
            elif cmd == ',': self.f6()
            elif cmd == '[': self.f7()
            elif cmd == '?': self.f8()
    def f1(self): self.i+=1
    def f2(self): self.i-=1
    def f3(self): self.stack[self.i]+=1
    def f4(self): self.stack[self.i]-=1
    def f5(self): print(chr(self.stack[self.i]), end='')
    def f6(self): self.stack[self.i]=ord(input()[0])
    def f7(self):
        print(bool(self.stack[self.i]))
        while self.stack[self.i]:
            self.interpret(Lexer(self.lexer.nextCharsTill(']')))
        else: print(bool(self.stack[self.i]))
    def f8(self): print(self.stack[self.i])
