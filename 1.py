#Задача No1. Решение в группах Семинар 1. Ввод-вывод, операторы ветвления
#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
#километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
#2

n = int (input('Сколько машина проезжает за день'))
m = int (input('Сколько километров нужно проехать')) 

result= (n + m -1) // n

print('Понадобиться', result, 'дней')