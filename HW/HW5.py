# 1. Абрамян: For 6, For 10
# 2. Прикрепленные задачки
# 3. Дополнительно: Ex 101 из первого учебника. Для нее потребуется почитать про пакет random питона и найти нужные фукнции

# For6
# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг конфет.
price = float(input())
for i in range(2, 10+1, 2):
    cost = (1 + i/10) * price
    print(f"Цена {1 + i/10} кг: {cost}")

# For10
# Дано целое число N (> 0). Найти сумму 1 + 1/2 + 1/3 + . . . + 1/N (вещественное число).
N = int(input("Введите число N: "))
summ = 0
for i in range(1, N+1):
    summ = summ + 1/i
    print(f"{summ}")

# Скриншот 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
a = 0
for i in range(1, 5+1):
    print(i, ".", a)

# Скриншот 2
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
a = 1
b = 100
summ = 0
for i in range(a, b+1):
    summ = summ + i
    print(summ)

# Ex.101
# In a particular jurisdiction, older license plates consist of three letters followed by three digits.
# When all of the license plates following that pattern had been used, the format was changed to four digits
# followed by three letters. Write a function that generates a random license plate. Your function should have
# approximately equal odds of generating a sequence of characters for an old license plate or a new license plate.
# Write a main program that calls your function and displays the randomly generated license plate.

from random import randint
plate = randint(1000, 9999)
import random
import string
def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))
print(plate, random_char(3))
