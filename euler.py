# coding=utf-8
__author__ = 'sford'

from math import sqrt


def multiples_of_3_and_5(num_count):
    # 1-я задача:
    # Находит сумму всех чисел меньше заданного числа, кратных 3 или 5.
    i = 1
    summ = 0
    while i < num_count:
        if (i % 3 == 0) or (i % 5 == 0):
            summ += i
        i += 1
    return summ


def sum_fibonacci_numbers(max_num):
    # 2-я задача:
    # Находит сумму всех четных элементов ряда Фибоначчи, которые не превышают заданного числа.
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
    # 3-я задача:
    # Находит самый большой делитель заданного числа, являющийся простым числом
    i = int(sqrt(num))  # Делитель не может быть больше квадратого корня заданного числа
    while i >= 1:
        if not (num % i):
            if prime_num(i):
                return i
        i -= 1
    return 0


def prime_num(num):
    # Проверяет на простое число
    i = 2
    while i < num:
        if not (num % i):
            return 0
        else:
            i += 1
    return num


def max_palindrome(num_size):
    # 4-я задача:
    # Находит самый большой палиндром, полученный умножением двух чисел заданного разряда.
    if num_size < 2:    # Проверка на разрядность для однозначных чисел
        return 0
    min_num = 10 ** (num_size - 1)  # Наименьшее значение полиндрома
    max_num = 10 ** num_size        # Наибольшее значение полиндрома
    palindrome = 0
    ra = range(max_num, min_num, -1)
    for i in ra:
        for j in ra:
            product = i * j
            if product > palindrome:
                s_product = str(product)
                if s_product == s_product[::-1]:    # Проверка на полиндромность
                    palindrome = product
    return palindrome


def evenly_divisible_min_num(num_count):
    # 5-я задача:
    # Ищем самое маленькое число, которое делится без остатка на все числа заданного кол-ва
    min_num = 2                                         # Число должно быть кратно двум
    i_num = range(num_count, int(num_count / 2), -1)    # И поэтому можно перебирать только пол диапазона
    for ii in i_num:                                    # Подсчитаем возможное минимальное число
        if prime_num(ii):
            min_num *= ii
    b_found = False
    while not b_found:                                  # Ищем то самое число
        for i in i_num:
            if min_num % i:
                min_num += 2                            # Шаг тоже может быть кратен двум
                break
        else:
            b_found = True
    return min_num

