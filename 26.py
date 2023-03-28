"""Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

a = int(input())
b = int(input())

def degree (a, b):
    res =1
    for i in  range (b):
        res *= a
    print(res) 

degree (a, b)    

def degree1 (a, b):
    if (b == 1):
        return (a)
    if b != 1:
      return a * degree1(a, b - 1)


res = degree1 (a, b) 
print(res)       