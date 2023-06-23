import signal
import sys
import time
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
        start_time = time.process_time()
        with open(filename) as f:
            numbers = f.read().splitlines()
            for num in numbers:
                num = int(num)
                factor1, factor2 = factorize(num)
                print("{}={:d}*{:d}".format(num, factor1, factor2))

        elapsed_time = time.process_time() - start_time
        print("\nreal    {:.3f}s".format(time.time() - start_time))
        print("user    {:.3f}s".format(elapsed_time))
        print("sys     {:.3f}s".format(elapsed_time))
        print("being   {:.3f}s".format(elapsed_time))
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
