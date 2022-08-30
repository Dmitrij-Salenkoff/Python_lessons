from math import sqrt


# Proc 3
#
#
# def mean(x: float, y: float) -> (float, float):
#     a_mean = (x + y) / 2
#     g_mean = sqrt(x * y)
#     return a_mean, g_mean
#
#
# A, B, C, D = list(map(float, input().split()))
# print(mean(A, B))
# print(mean(A, C))
# print(mean(A, D))


# Proc 56
#
#
# def leng(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     return sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)
#
#
# x1, y1, x2, y2 = list(map(float, input().split()))
# print(leng(x1, y1, x2, y2))

# Proc 57

# def leng(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     return sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)
#
#
# def perim(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     return AB + AC + BC

# print(perim(0, 0, 0, 3, 4, 0))

# Proc 58

# def leng(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     return sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)
#
#
# def perim(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     return AB + AC + BC
#
#
# def area(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     return S
#
#
# print(area(0, 0, 0, 3, 4, 0))
