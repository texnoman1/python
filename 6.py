'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

385916 -> yes
123456 -> no
'''

num = int (input('Введите 6 цифр номера билета   '))

first3digits = 0
last3digits = 0
temp = 0

for i in range (3):
    temp = num % 10
    last3digits += temp
    num = num // 10
for i in range (3):
    temp = num % 10
    first3digits += temp
    num = num // 10
if first3digits ==  last3digits:
    print('yes')
else:
    print('no')      