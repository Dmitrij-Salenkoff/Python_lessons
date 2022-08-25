# Абрамян: Series 2, Series 7 (round), Series 15, Series 23

# Series2
# Даны десять вещественных чисел. Найти их произведение.
lst = list(map(float, input("Введите набор вещественных чисел: ").split()))
print(lst)
N = 10
product = 1
for i in range(N):
    product = product * lst[i]
print(product)

# Series15
# Дано целое число K и набор ненулевых целых чисел; признак его завершения — число 0.
# Вывести номер первого числа в наборе, большего K. Если таких чисел нет, то вывести 0.
K = int(input("Введите число К: "))
lst = list(map(int, input("Введите набор ненулевых чисел: ").split()))
ans = []
for i in range(1, len(lst)):
    if lst[i] > K:
        ans.append(lst[i])
print(ans)
print(len(ans))

# Series7 (round)
#  Дано целое число N и набор из N вещественных чисел. Вывести в том же порядке округленные значения всех чисел
#  из данного набора (как целые числа), а также сумму всех округленных значений

# round(float_number, number_of_decimals) - округление до целого числа
# number_of_decimals - числа после запятой
# Если >= 5, то добавляется +1.
# Если <5, то финальное значение такое же, как и до десятых.

lst = list(map(float, input().split()))
# N = int(input("Введите число N: "))
summ = 0
for i in range(len(lst)):
    print(round(lst[i]))
    summ = summ + lst[i]
print(round(summ))


# Series23
# Дано целое число N (> 2) и набор из N вещественных чисел.
# Набор называется пилообразным, если каждый его внутренний элемент либо больше, либо меньше обоих своих соседей
# (то есть является «зубцом»). Если данный набор является пилообразным, то вывести 0;
# в противном случае вывести номер первого элемента, не являющегося зубцом.
lst = list(map(float, input().split()))
# N = int(input("Введите число N: "))
# if N > 2:
#     print(True)
# else:
#     print(False)
ans = []
for i in range(1, len(lst)):
    if lst[i-1] < lst[i]:
        ans.append(lst[i])
    elif lst[i] > lst[i+1]:
        ans.append(lst[i])
    elif lst[i-1] > lst[i]:
        ans.append(lst[i])
    elif lst[i] > lst[i+1]:
        ans.append(lst[i])
print(ans)
print(len(ans))
