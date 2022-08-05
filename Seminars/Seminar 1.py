# # Bool - Boolean - логический тип данных: True or False
# a = True
# c = True
# b = False

# print(a) # print - печатать
# print(type(a)) # type - вернуть тип объекта

# c = a or b # True or False = True |
# d = a and b # True and False = False &
# e = not a # not True = False
#
# print(c, d, e)

# int - integer - целое число: 1, 0, -100, 200
# a = 10
# b = 2
#
# print(a, b)
# print(type(a))
#
# print(a + b, a - b, a * b, a / b)
# # a / b - возвращает число с плавающей запятой -> float
#
# print(a // b)  # // - целочисленное деление -> int
# print(type(a / b), type(a // b))
#
# print(10 % 3) # % - нахождение остатка от деления 14 % 5 = 4
# print(abs(-5)) # abs - absolute value - модуль числа
#
# print(a ** b) # ** - возведение в степень  10 ** 2 = 100
# print(pow(a, b)) # - тоже самое


# float - Floating point - число с плавающей запятой - любое не целое число
# 3.14, 2.11111111, -0.1

# Действия все те же самые как и int

# Операции сравнения:
# print(1 < 2)
# print(10 > 20)
# print(2 <= 10)
# print(10 >= 1)
# print(10 == 10)
# print(10 == 1)
# print(10 != 1)
# print(True is None)

# None - "ничего"

# str - String - строка. Пишется в кавычках "" или ''
# "abc", '123', "", ' ', ".", ',,,,,'
# a = 'abcdeg'
# b = "123"
# print(a + b, a[0])
# print("c" in a)
# print(a * 10)
# print(a[2:5])
# print(len(a)) # len - lenght - длина строки



# input() - Ввод с клавиатуры - по умолчанию все в строки
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# print("Произведение чисел равно: ", a * b)


# Exercise 1
# Create a program that displays your name and complete mailing address. The address
# should be printed in the format that is normally used in the area where you live. Your
# program does not need to read any input from the user.

# print('Dima')
# print('email: dmitrij.salenkoff@gmail.com')


# Exercise 3
# Write a program that asks the user to enter the width and length of a room. Once
# these values have been read, your program should compute and display the area of
# the room. The length and the width will be entered as floating-point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

# width = float(input('Enter the width (in m):'))
# lenght = float(input('Enter the length (in m):'))
# area = width * lenght
# print(area, ' m^2')


# Exercise 5
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and two digits to the right of the decimal point.

# bottles_small = int(input("Enter the number of small bottles: "))
# bottles_big = int(input("Enter the number of big bottles: "))
# small_deposit = 0.10
# big_deposit = 0.25
# summ_deposit = bottles_small * small_deposit + bottles_big * big_deposit
# print(summ_deposit, "$")


# Exercise 7
# n = int(input("Enter the n: "))
# summ = n * (n + 1) / 2
# print('Sum of the integers from 1 to n: ', int(summ))







