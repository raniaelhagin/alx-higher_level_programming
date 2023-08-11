#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argvalues = sys.argv
    argv_len = len(argvalues)

    if argv_len == 1:
        print("0 arguments.")
    elif argv_len == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argv_len - 1))

    for i in range(1, argv_len):
        print("{:d}: {:s}".format(i, argvalues[i]))
