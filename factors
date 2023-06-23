#!/usr/bin/python3
import sys
import subprocess
import time
import resource
from math import isqrt

def factorize_number(n):
    """
    Factorizes a given number into a product of two smaller numbers.
    Returns the factors if found, None otherwise.
    """
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    return None

def factorize_file(filename):
    """
    Factorizes numbers from a given file.
    Prints the factorization for each number found.
    """
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize_number(number)
            if factors is not None:
                p, q = factors
                print(f"{number}={p}*{q}")
            else:
                print(f"{number} is a prime number.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        file_path = sys.argv[1]

        start_time = time.time()
        start_user_time, start_sys_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime, resource.getrusage(resource.RUSAGE_SELF).ru_stime

        # Print the factorization results
        factorize_file(file_path)

        elapsed_time = time.time() - start_time
        elapsed_user_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime - start_user_time
        elapsed_sys_time = resource.getrusage(resource.RUSAGE_SELF).ru_stime - start_sys_time

        # Print the time output
        print(f"real\t{elapsed_time:.3f}s")
        print(f"user\t{elapsed_user_time:.3f}s")
        print(f"sys\t{elapsed_sys_time:.3f}s")
