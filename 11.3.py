"""Валентина прогуляла лекцию по математике. 
Преподаватель решил подшутить над нерадивой студенткой и 
попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел. 
Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось. 
На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

Решить такое вручную, как вы понимаете, практически нереально. 
Вот Валентина и обратилась к вам за помощью. 
Помогите ей (при помощи функции all_divisors(number))."""

n = int(input('Введите число:\n'))

for num in range(2, n + 1):
    if n % num != 0:
        continue
    flag = True
    for spam in range(num - 1, 1, -1):
        if num % spam == 0:
            flag = False
            break
    if flag:
        print(num, end=' ')