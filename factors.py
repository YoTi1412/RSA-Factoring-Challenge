#!/usr/bin/python3
import signal
import sys
from math import isqrt


def factorize(value):
    for i in range(2, isqrt(value) + 1):
        if value % i == 0:
            return i, value // i
    return value, 1


def factors():
    def timeout_handler(signum, frame):
        raise TimeoutError("Program execution exceeded time limit")

    # Set the signal handler for the alarm
    signal.signal(signal.SIGALRM, timeout_handler)
    # Set the alarm for 5 seconds
    signal.alarm(5)

    try:
        filename = sys.argv[1]
        with open(filename) as f:
            for line in f:
                num = int(line.strip())
                factor1, factor2 = factorize(num)
                print("{}={:d}*{:d}".format(num, factor1, factor2))
    except TimeoutError:
        print("Error: Program execution exceeded time limit")
    except IndexError:
        print("Error: No input file provided")
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Invalid input, expected natural numbers")
    except Exception as e:
        print("Error:", str(e))


factors()