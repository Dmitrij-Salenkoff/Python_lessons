# # Абрамян: Series 2, Series 7 (round), Series 15, Series 23
#
# # Series2
# # Даны десять вещественных чисел. Найти их произведение.
# lst = list(map(float, input("Введите набор вещественных чисел: ").split()))
# print(lst)
# N = len(lst)
# product = 1
# for i in range(N):
#     product = product * lst[i]
# print(product)

#
# # Series15
# # Дано целое число K и набор ненулевых целых чисел; признак его завершения — число 0.
# # Вывести номер первого числа в наборе, большего K. Если таких чисел нет, то вывести 0.
# K = int(input("Введите число К: "))
# lst = list(map(int, input("Введите набор ненулевых чисел: ").split()))
# ans = []
# for i in range(1, len(lst)):
#     if lst[i] > K:
#         ans.append(lst[i])
# if len(ans) > 0:
#     print(ans[0])
# else:
#     print(0)
#

# # Series7 (round)
# #  Дано целое число N и набор из N вещественных чисел. Вывести в том же порядке округленные значения всех чисел
# #  из данного набора (как целые числа), а также сумму всех округленных значений
#
# # round(float_number) - округление до целого числа
# # round(float_number, number_of_decimals) - округление до десятичного знака под номером number_of_decimals
# # number_of_decimals - числа после запятой
# # Если >= 5, то добавляется +1.
# # Если <5, то финальное значение такое же, как и до десятых.

# lst = list(map(float, input().split()))
# # N = int(input("Введите число N: "))
# summ_1 = 0
# summ_2 = 0
# for i in range(len(lst)):
#     print(round(lst[i]))
#     summ_1 = summ_1 + round(lst[i])
#     summ_2 = summ_2 + lst[i]
# print(summ_1)
# print(round(summ_2))

# # Series23
# # Дано целое число N (> 2) и набор из N вещественных чисел.
# # Набор называется пилообразным, если каждый его внутренний элемент либо больше, либо меньше обоих своих соседей
# # (то есть является «зубцом»). Если данный набор является пилообразным, то вывести 0;
# # в противном случае вывести номер первого элемента, не являющегося зубцом.
# lst = list(map(float, input().split()))
# # N = int(input("Введите число N: "))
# # if N > 2:
# #     print(True)
# # else:
# #     print(False)
# ans = []
# flag = True
# for i in range(1, len(lst)-1):
#     if not ((lst[i] > lst[i-1] and lst[i] > lst[i+1]) or (lst[i] < lst[i-1] and lst[i] < lst[i+1])):
#         print(i)
#         flag = False
#         break
# if flag:
#     print(0)
