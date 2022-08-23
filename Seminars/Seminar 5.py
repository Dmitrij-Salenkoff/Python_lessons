# list - список
# lst_1 = [1, 'a', None, True, 3.14, False, 1, 6]
# lst_2 = [4, 3, 2]
#
# print(lst_1 + [10])

# lst = ['2', '3', '4']

# lst.append('5')
#
# string = "$".join(lst)
#
# print(string)

# Series1◦
#
# . Дан список вещественных чисел. Найти их сумму

# lst = list(map(float, input().split()))
# summ = 0
# for i in range(len(lst)):
#     summ = summ + lst[i]
# print(summ)

# lst = list(map(float, input().split()))
# print(sum(lst))

# print(sum(list(map(float, input().split()))))

# Series3.
# Дан список вещественных чисел. Найти их среднее арифметическое.

# lst = list(map(float, input().split()))
# N = len(lst)
# summ = 0
# count = 0
# for i in range(N):
#     summ = summ + lst[i]
#     count = count + 1
# print(summ / count)

# lst = list(map(float, input().split()))
# print(sum(lst) / len(lst))

# Series19◦
#
# . Дан набор из N целых чисел. Вывести те
# элементы в наборе, которые меньше своего левого соседа, и количество K
# таких элементов.
#
# lst = list(map(float, input().split()))
# ans = []
#
# for i in range(1, len(lst)):
#     if lst[i-1] > lst[i]:
#         ans.append(lst[i])
# print(ans)
# print(len(ans))

# Series21◦
#
# . Дан набор из N вещественных чисел. Прове-
# рить, образует ли данный набор возрастающую последовательность. Если
# образует, то вывести TRUE, если нет — вывести FALSE.

# 1 4 7 9 11 14 16 - Возрастающая
# 9 7 5 3 1 - Убывающая

# lst = list(map(float, input().split()))
# flag = True
# for i in range(1, len(lst)):
#     if lst[i-1] >= lst[i]:
#         flag = False
#         break
# print(flag)


# Series24. Дан набор из N целых чисел, содержащий по
# крайней мере два нуля. Вывести сумму чисел из данного набора, распо-
# ложенных между последними двумя нулями (если последние нули идут
# подряд, то вывести 0).

lst = list(map(float, input().split()))
zeros = []
for i in range(len(lst)):
    if lst[i] == 0:
        zeros.append(i)
a = zeros[-2]
b = zeros[-1]
# summ = 0
# for i in range(a, b+1):
#     summ = lst[i]
print(sum(lst[a:b+1]))

