"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A i
. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""
from random import randint

n = int (input("enter the number of elements N in the array - "))
x = int (input("Enter the number X - "))

a = [randint(0, 10) for i in range(n) ]

print(a)
for j in range (x):
    for i in range (len(a)):
        b = j
        if a[i]== x - b or a[i] == x + b:
            print(a[i])
            quit()    # выход сразу из двух циклов, break не работает
       