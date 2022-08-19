# For4. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1,
# 2, . . . , 10 кг конфет.

# price = float(input())
#
# for i in range(1, 10+1):
#     cost = i * price
#     print(f'Цена {i} кг: {cost}')

# For5◦
# . Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1,
# 0.2, . . . , 1 кг конфет.

# price = float(input())
#
# for i in range(1, 10+1):
#     cost = (i/10) * price
#     print(f'Цена {i/10} кг: {cost}')

# For8. Даны два целых числа A и B (A < B). Найти произведение всех целых
# чисел от A до B включительно.

# A = int(input())
# B = int(input())
#
# prod = 1
#
# for i in range(A, B+1):
#     prod = prod * i
# print(prod)

# For14. Дано целое число N (> 0). Найти квадрат данного числа, используя для
# его вычисления следующую формулу:
#
# N**2 = 1 + 3 + 5 + . + N + . . + (2·N − 1).
# 4**2 = 1 + 3 + 5 + 7 = 16
# После добавления к сумме каждого слагаемого выводить текущее значе-
# ние суммы (в результате будут выведены квадраты всех целых чисел от 1 до N).

# N = int(input())
# sqr = 0
# for i in range(1, 2*N, 2):
#     sqr = sqr + i
# print(sqr)

# from math import factorial, exp
#
# X = float(input())
# N = int(input())
#
# summ = 1
#
# for i in range(1, N+1):
#     summ = summ + X**i / factorial(i)
# print(f'Из math: {exp(X)} \n Наше: {summ}')
#
# # e = 2.71828128459045
# # exp(x) = e**x

# F1 = 1, F2 = 1
# F3 = F1 + F2 = 2
# F4 = F2 + F3 = 3
# F5 = F3 + F4 = 5

N = int(input())

F1 = 1
F2 = 1
print(F1)
print(F2)
prev_1 = F1
prev_2 = F2
for i in range(3, N+1):
    next = prev_1 + prev_2
    print(next)
    prev_1 = prev_2
    prev_2 = next
