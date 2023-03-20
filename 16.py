"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A i
. Последняя строка содержит число X 

Метод sequence.count() позволяет узнать сколько раз указанный элемент x появился в последовательности sequence.

Результатом будет целое число, показывающее количество вхождений элемента x в последовательность sequence.

Другими словами, сколько раз указанный элемент x появляется в последовательности или сколько раз встречается буква/символ/подстрока в какой либо строке.


5
1 2 3 4 5
3
-> 1"""

from random import randint

n = int (input("enter the number of elements N in the array - "))
x = int (input("Enter the number X - "))

a = [randint(0, 10) for i in range(n) ]


count = 0
for i in range (len(a)):
    if a[i] == x:
        count += 1


print(a)
print(count)
print(a.count(x))



   
