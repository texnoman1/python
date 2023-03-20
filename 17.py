"""Задача No17. Общее обсуждение Дан список чисел. Определите, сколько в нем
встречается различных чисел. Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6"""

k = int(input('Укажите сдвиг'))
values = [1, 2, 3, 4, 5]
length = len(values)
k = k % length
print(values)
print(values[-k:] + values[:-k])

variant2
k = 3
list_1 = [1, 2, 3, 4, 5]
j = 0
list_2 = [0]*len(list_1)

for i in range(len(list_1)):
j = (i + k) % len(list_1)
list_2[i] = list_1[j]
i = i +1

print(list_2)