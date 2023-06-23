#!/usr/bin/python3
import sys

if __name__ == "__main__":
    with open(sys.argv[1], "r") as fd:
        readlins = fd.readlines()
    for line in readlins:
        num = int(line)
        diviser = 2
        while (num % diviser != 0):
            diviser += 1
        print("{}={}*{}".format(num, int((num / diviser)), diviser))
