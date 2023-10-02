#!/usr/bin/python3
"""A function that reads a text file and prints its content to stdout"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
