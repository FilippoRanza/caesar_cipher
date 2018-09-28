#! /usr/bin/python

from caesar_cipher.caesar_runner_lib.runner import Runner
from caesar_cipher.caesar_crypto_lib.probabily_vector import get_default, available_lang, probability_vector
from caesar_cipher.caesar_crypto_lib.caesar_analysis import prob_analysis
from caesar_cipher.caesar_crypto_lib.caesar_cipher import CaesarDecrypt
from caesar_cipher.caesar_runner_lib.formatter import print_table


class Crack(Runner):

    def _crack_code_(self):
        crypto = self.in_file.read()
        k, dv = prob_analysis(crypto, probability_vector[self.lang])
        decrypt = CaesarDecrypt(crypto)
        decrypt.decrypt(k)
        self.out_file.write(decrypt.get_text())

        print("Key:", k)
        print_table(dv)

    def _parse_args_(self):
        args = super()._parse_args_()
        if args.lang:
            self.lang = args.lang
        if args.avail:
            self.list = args.avail

    def run(self):
        self._parse_args_()
        if self.list:
            for i in available_lang():
                print(i)
        else:
            self._crack_code_()

    def __init__(self):
        super().__init__()

        self.lang = get_default()
        self.list = False

        self.parse.add_argument('-l', '--lang',
                                default=self.lang,
                                help='set original message language',
                                type=str)
        self.parse.add_argument('-a', '--avail',
                                default=self.list,
                                help='list available languages and exit',
                                type=bool)

        self.f = self._crack_code_
