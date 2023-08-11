#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv
    argc = len(arguments)

    result = 0
    for i in range(1, argc):
        result += int(arguments[i])
    print(result)
