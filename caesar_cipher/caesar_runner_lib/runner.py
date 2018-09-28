#! /usr/bin/python
import argparse
import sys


class BackupNameGenerator:

    def next(self):

        if self.n == 0:
            out = 'bak'
        else:
            out = "bak_%d" % self.n

        self.n += 1
        return out

    def __init__(self):
        self.n = 0


def make_output_name(in_name):
    from os.path import exists
    from os import rename
    out_name = "%s.out" % in_name
    if exists(out_name):
        prev = out_name
        generator = BackupNameGenerator()

        while exists(prev):
            tmp = generator.next()
            rename(prev, tmp)
            prev = tmp

    return out_name


class Runner:

    def _parse_args_(self):
        args = self.parse.parse_args()

        if args.input:
            self.in_file = open(args.input, 'r')
            if args.output:
                self.out_file = open(args.output, 'w')
            else:
                out_name = make_output_name(args.input)
                self.out_file = open(out_name, 'w')
        else:
            self.in_file = sys.stdin
            self.out_file = sys.stdout

        return args

    def run(self):
        pass

    def __init__(self):

        self.parse = argparse.ArgumentParser()
        self.parse.add_argument('-i', '--input',
                                help='set input file name',
                                required=False,
                                type=str)
        self.parse.add_argument('-o', '--output',
                                help='output file name',
                                required=False,
                                type=str)

        self.in_file = None
        self.out_file = None

