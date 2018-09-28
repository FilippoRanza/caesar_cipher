#! /usr/bin/python


def print_head():
    print("Key|Point")
    print("---+-----")


def print_point(k, p):
    msg = "%3d|%f" % (k, p)
    print(msg)


def print_table(dv):
    keys = {}
    for i, v in enumerate(dv):
        keys[v] = i + 1

    print_head()
    dv.sort()
    for i in dv:
        print_point(keys[i], i)
    print("lower is better")



