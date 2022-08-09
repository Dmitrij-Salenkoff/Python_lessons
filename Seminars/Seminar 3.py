# while
# for i in range(N)

# a = 0
# while a < 10:
#     a = a + 1
#     print(f'Значение а равно: {a}')
#
# print('Мы вышли из цикла')

# a = 0
# while True:
#     a = a + 1
#     print(a)
#     if a == 10:
#         print('Out of loop')
#         break

# [1, 2, 3, None, 'a', 'absadf', False, 1.01] - iterable
# range(N) - iterable - генерирует числа от 0 до N
# range(10) ~ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(3, 10) ~ [3, 4, 5, 6, 7, 8, 9]
# range(3, 10, 2) ~ [3, 5, 7, 9]

# for i in range(10):
#     for j in range(10):
#         print(f'{i} - {j}')

# Ex 63
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.

# # average = sum / count
# sum = 0
# count = 0
#
# a = int(input())
# # if a == 0:
# #     print('Error')
# # else:
# #     sum = sum + a
# #     count = count + 1
#
# while True:
#     a = int(input())
#     if a == 0 and count == 0:
#         print('Error')
#         break
#     elif a == 0:
#         break
#     else:
#         sum = sum + a
#         count = count + 1
#
# if count > 0:
#     print(sum / count)

# Ex 65
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the Internet.

# F = 1.8 * C + 32

# for i in range(0, 101, 10):
#     print(f'Celsius: {i} - Fahrenheit: {1.8 * i + 32}')

# Ex 71
# pi = 3
# print(pi)
#
# for i in range(2, 10000000, 2):
#     power = (i // 2) + 1
#     pi = pi + (4 / (i * (i+1) * (i+2))) * (-1)**power
#     print(pi)

# Ex 77

# N = 20
# for i in range(0, N+1):
#     print(i, end='\t')
# print()
#
# for i in range(1, N+1):
#     print(i, end='\t')
#     for j in range(1, N+1):
#         print(i*j, end='\t')
#     print()




