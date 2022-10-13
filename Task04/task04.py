# 4. Задайте список из элементов, заполненных числами из промежутка [-N, N]. 
# Задайте два числа - позиции(индексы) в исходном списке это границы диапазона. 
# Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16

# Задайте список из элементов, заполненных числами из промежутка [-N, N]. 
n = int(input('Введите число организации списка: '))
import random
number_list = []
i = 0
for i in range (0, n*2):
    el = random.randint(-n, n)
    number_list.append(el)
    i += 1

print(number_list)

# Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
start_i = int(input('Введите начальный индекс: '))
finish_i = int(input('Введите финальный индекс: '))
mult_list = []

if start_i > n*2 or finish_i > n*2: 
    print('Один или оба индекса не существуют в списке')
elif start_i < finish_i:
    for i in range (start_i, finish_i):
        mult_list.append(number_list[i])
else:
    for i in range (finish_i, start_i):
        mult_list.append(number_list[i])

# Найдите произведение элементов списка в указанном диапазоне индексов
result = 1
for el in mult_list:
    result = result * el

print('Результат умножения заданной области списка:', result)




# elif start_i < finish_i:
#     for i in range (number_list[start_i], number_list[finish_i + 1]):
#         multiple = multiple * number_list[i]
#     print(multiple)
# else:
#     for i in range (finish_i, start_i + 1):
#         multiple = multiple * i
#     print(multiple)