"""Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
"""
a = int (input("Введите число a  "))
b = int (input("Введите число b  "))

def sum (a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

print(sum(a, b))

def rec_sum(a, b):
   return a if b == 0 else rec_sum(a+1, b-1) #if b > 0 else rec_sum(a-1, b+1)

print(rec_sum(a, b))