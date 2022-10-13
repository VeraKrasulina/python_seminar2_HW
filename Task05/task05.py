# 5. Реализуйте алгоритм перемешивания элементов списка. Без функции shuffle из модуля random, другие методы использовать можно.


n = int(input('Введите число организации списка: '))
import random
number_list = []
i = 0
for i in range (0, n*2):
    el = random.randint(-n, n)
    number_list.append(el)
    i += 1

print(number_list)

iteration = random.randint(2, 100)
temp_el = 0
while iteration > 0:
    for i in range(0, len(number_list)):
        for j in range(0, len(number_list) - i):
            temp_el = number_list[i]
            number_list[i] = number_list[j]
            number_list[j] = temp_el
        iteration -= 1

print(number_list)

