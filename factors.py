#!/usr/bin/python3
import signal
import sys
from math import sqrt


def factor():
    def timeout_handler(signum, frame):
        raise TimeoutError("Program execution exceeded time limit")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)

    try:
        filename = sys.argv[1]
        with open(filename) as f:
            for line in f:
                num = int(line)
                print("{:d}=".format(num), end="")
                if num % 2 == 0:
                    print("{}*2".format(num // 2))
                    continue
                sqn = int(sqrt(num))
                if sqn % 2 == 0:
                    sqn += 1
                for i in range(3, sqn + 1, 2):
                    if num % i == 0:
                        print("{}*{}".format(i, num // i))
                        break
                if num % i != 0:
                    print("{}={}*1".format(num, num))
    except TimeoutError as e:
        print("Error: Program execution exceeded time limit")
    except IndexError:
        print("Error: No input file provided")
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print("Error:", str(e))
    finally:
        signal.alarm(0)


factor()
