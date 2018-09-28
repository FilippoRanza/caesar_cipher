#! /usr/bin/python

import sys
from caesar_cipher import Crypt, Decrypt, Crack, Helper

module = {
    'crypt': Crypt,
    'decrypt': Decrypt,
    'crack': Crack,
    'help': Helper
}


def get_module():
    if len(sys.argv) == 1:
        out = Helper
    else:
        out = module[sys.argv[1]]
        sys.argv.pop(1)

    return out


if __name__ == '__main__':
    module = get_module()
    o = module()
    o.run()


