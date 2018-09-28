#! /usr/bin/python

from caesar_cipher.caesar_runner_lib.runner import Runner


class Helper(Runner):

    def run(self):
        print("crypt: encrypt given text")
        print("decrypt: decrypt given text")
        print("crack: analyze and crack given crypto text")
        print("help: show this help and exit")
