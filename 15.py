"""15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9"""

n = int(input("Введите количество арбузов в сетке: "))
watermellons = [0] * n
index = 0
while index < n:
    watermellons[index] = int(input("Введите массу арбуза в сетке: "))
    index +=1

print(f"Массы арбузов в сетке {watermellons}")

max = watermellons[0]
min = watermellons[0]
for i in watermellons:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Масса самого тяжелого арбуза равна {max} кг")
print(f"Масса самого легкого арбуза равна {min} кг")