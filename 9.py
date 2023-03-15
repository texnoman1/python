number = int(input("Введите целое число >= 0: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1

print(factorial)