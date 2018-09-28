#! /usr/bin/python

"""
A simple caesar's cipher implementation
"""

from .tokenizer import Tokens


class CaesarCipher:

    def _compute_(self, k):
        self.tokens.apply(lambda x: self.f(x, k, self.lc))

    def get_text(self):
        return self.tokens.get_text()

    def __init__(self, txt, f, lc=26):
        self.lc = lc
        self.f = f
        self.tokens = Tokens(txt, lc=lc)


class CaesarCrypt(CaesarCipher):

    def __init__(self, txt, lc=26):
        super().__init__(txt, lambda n, k, c: (n + k) % c, lc)

    def encrypt(self, k):
        self._compute_(k)


class CaesarDecrypt(CaesarCipher):

    def __init__(self, txt, lc=26):
        super().__init__(txt, lambda n, k, c: (n - k) % c, lc)
        self.lc = lc
        self.k = 0

    def decrypt(self, k):
        self._compute_(k)

    def __iter__(self):
        self.k = 0
        return self

    def __next__(self):
        if self.k == self.lc:
            raise StopIteration

        self.decrypt(1)
        self.k += 1
        return self.tokens
