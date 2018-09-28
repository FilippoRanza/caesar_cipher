#! /usr/bin/python


class Tokens:

    def _map_to_text(self, t):
        out = ""
        for w in t:
            tmp = map(lambda x: self.to_letter[x], w)
            out += "".join(tmp) + " "
        return out

    def get_text(self):

        out = ""
        for t in self.tokens:
            out += self._map_to_text(t)
            out += "\n"
        return out

    def _map_to_digit(self, t):
        tmp = map(lambda l: list(map(lambda x: self.to_digit[x], l)), t)
        return list(tmp)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.tokens):
            out = self.tokens[self.i]
            self.i += 1
            return out
        else:
            raise StopIteration

    def apply(self, f):
        for line in self.tokens:
            for t in line:
                for i, v in enumerate(t):
                    t[i] = f(v)

    def analyze(self, f):
        for line in self.tokens:
            for t in line:
                f(t)

    def __init__(self, txt, lc=26):

        self.to_digit = {}
        self.to_letter = [None] * lc
        self.i = 0
        for i in range(lc):
            n = ord('a') + i
            c = chr(n)
            self.to_letter[i] = c

        for i in range(lc):
            l = chr(ord('a') + i)
            U = chr(ord('A') + i)

            self.to_digit[l] = i
            self.to_digit[U] = i

        tmp = txt.split('\n')
        flt = list(filter(lambda x: len(x) != 0, map(lambda x: x.split(), tmp)))
        self.tokens = [None] * len(flt)
        for i, t in enumerate(flt):
            self.tokens[i] = self._map_to_digit(t)



