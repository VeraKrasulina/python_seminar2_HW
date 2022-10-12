# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44

number = str(input('Введите вещественное число: '))
number_temp = number.replace('.', '')
number = int(number_temp)

sum = 0
while number > 0:
    sum += number % 10
    number //= 10

print(sum)