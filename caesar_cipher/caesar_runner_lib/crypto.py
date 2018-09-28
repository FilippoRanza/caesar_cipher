#! /usr/bin/python

from caesar_cipher.caesar_runner_lib.runner import Runner
from caesar_cipher.caesar_crypto_lib.caesar_cipher import CaesarCrypt, CaesarDecrypt


class Cipher(Runner):

    def _parse_args_(self):
        args = super()._parse_args_()
        if args.key:
            self.k = args.key

    def run(self):
        self._parse_args_()
        txt = self.in_file.read()
        out = self.f(txt)
        self.out_file.write(out)

    def __init__(self):
        super().__init__()
        self.k = 3
        self.parse.add_argument('-k', '--key',
                                help='key value',
                                default=self.k,
                                type=int)

        self.f = None


class Crypt(Cipher):

    def _crypt_(self, txt):
        crypto = CaesarCrypt(txt)
        crypto.encrypt(self.k)
        return crypto.get_text()

    def __init__(self):
        super().__init__()
        self.f = self._crypt_


class Decrypt(Cipher):

    def _decrypt_(self, txt):
        crypto = CaesarDecrypt(txt)
        crypto.decrypt(self.k)
        return crypto.get_text()

    def __init__(self):
        super().__init__()
        self.f = self._decrypt_


