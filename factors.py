#!/usr/bin/python3
"""Module that factorize as many numbers as possible
 into a product of two smaller numbers."""
from sys import argv


def factorize(value):
    """"print a simple descomposition of an integer > 1"""
    i = 2

    if value < 2:
        return
    while value % i:
        i += 1
    print("{:.0f}={:.0f}*{:.0f}".format(value, value / i, i))


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Skip empty lines
                value = int(line)
                factorize(value)
except:
    pass
