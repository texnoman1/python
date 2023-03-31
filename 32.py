"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

Диапазон от 6 до 12

Вывод: [1, 9, 13, 14, 19]

"""

str = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
max = 12
min = 6

def ind(str, max, min):
    res = []
    for i in range(len(str)):
        if str[i] > min and str[i] < max:
            res.append(i)

            #print(i, end = " ")
        #print(str[i], end = " ")
    #print(res)
    return res

print(ind(str, max, min))   