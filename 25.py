"""Задача No25. Решение в группах Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. 
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
Синтаксис: list.count(x). Метод count() принимает один аргумент x, значение которое нужно найти. Данный метод возвращает количество вхождений элемента в список.
"""

str = "a a a b c a a d c d d" # str = "a a a b c a a d c d d".split(" ")
str = str.split(" ")

for i in range(len(str)):
    str1 = str[:i+1]
    count = str1.count(str[i])
    
    if count > 1:
        print(str1[i], "_",count-1, end='  ')
    else:
        print(str1[i], end='  ')
    

Алексей: str_list = input().split()

set_str = set(str_list)

for i in set_str:
count = 0
for s in range(len(str_list)):
if i == str_list[s]:
if count >= 1:
str_list[s] = str_list[s] + "_" + str(count)
count += 1

print (str_list)

Ришат: s = input('Please input text: ').split()
d = {}

for i in s:
if i in d:
d[i] += 1
else:
d[i] = 1
print(f"{i}", end="")
if d[i] > 1:
print(f"_{d[i]}", end=" ")
else:
print(' ', end="")
