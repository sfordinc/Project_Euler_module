__author__ = 'sford'

from math import sqrt


def multiples_of_3_and_5(num_count):
    i = 1
    summ = 0
    while i < num_count:
        if (i % 3 == 0) or (i % 5 == 0):
            summ += i
        i += 1
    return summ


def sum_fibonacci_numbers(max_num):
    summ = 0
    fib_num = 0
    fi = fib_num
    si = 1
    while fib_num <= max_num:
        fib_num = fi + si
        fi = si
        si = fib_num
        if not (fib_num % 2):
            summ += fib_num
    return summ


def max_prime_factor(num):
    i = int(sqrt(num))
    while i >= 1:
        if not (num % i):
            if prime_num(i):
                return i
        i -= 1
    return 0


def prime_num(num):
    i = 2
    while i < num:
        if not (num % i):
            return 0
        else:
            i += 1
    return num