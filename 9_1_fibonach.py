

n = int(input("Введите натуральное число N "))
index = 3
fib_1 = 0
fib_2 = 1
fib_current = 1
temp = 1
while fib_current < n:
    temp = fib_current
    fib_current = fib_1 + fib_current
    fib_2 = fib_1
    fib_1 = temp
    index += 1

if fib_current == n:
    print(f"Это {index-1} число Фибоначчи")
else:
    print(f"Такого числа Фибоначчи не существует")