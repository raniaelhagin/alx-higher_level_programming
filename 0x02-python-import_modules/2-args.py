#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argvalues = sys.argv[1:]
    argv_len = len(argvalues)

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
        print("1: ", argvalues[0])
    else:
        print("{:d} arguments:".format(argv_len))
        for i in range(1, argv_len + 1):
            print("{:d}: {:s}".format(i, argvalues[i - 1]))
