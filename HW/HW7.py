# Proc59
from math import sqrt
# def leng(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     return sqrt((x_a - x_b)**2 + (y_a - y_b)**2) # находим стороны
#
# def perim(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     return AB + AC + BC # периметр
#
# def area(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     return S
#
# def dist(x_p: float, y_p: float, x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     PA = leng(x_p, y_p, x_a, y_a)
#     PB = leng(x_p, y_p, x_b, y_b)
#     AB = leng(x_a, y_a, x_b, y_b)
#     P = perim(x_p, y_p, x_a, y_a, x_b, y_b) / 2
#     S = sqrt(P * (P - PA) * (P - PB) * (P - AB))
#     D = 2 * S / AB # здесь должен быть модуль AB, но если число >= 0, то при раскритии число остается таким же.
#     return D
#
# print(dist(0, 0, 0, 3, 4, 0))

# proc60
# def leng(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     return sqrt((x_a - x_b)**2 + (y_a - y_b)**2)
#
# def perim(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     return AB + AC + BC
#
# def area(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     return S
#
# def dist(x_p: float, y_p: float, x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AP = leng(x_p, y_p, x_a, y_a)
#     BP = leng(x_p, y_p, x_b, y_b)
#     P = perim(x_p, y_p, x_a, y_a, x_b, y_b) / 2
#     S = sqrt(P * (P - AP) * (P - BP) * (P - AB))
#     D = 2 * S / AB
#     return D
#
# def heights(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     # AB = leng(x_a, y_a, x_b, y_b)
#     # AC = leng(x_a, y_a, x_c, y_c)
#     # BC = leng(x_b, y_b, x_c, y_c)
#     # P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     # S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     # D = 2 * S
#     # HA = D / BC
#     # HB = D / AC
#     # HC = D / AB
#     HA = dist(x_a, y_a, x_b, y_b, x_c, y_c)
#     HB = dist(x_b, y_b, x_a, y_a, x_c, y_c)
#     HC = dist(x_c, y_c, x_a, y_a, x_b, y_b)
#     return HA, HB, HC
# print((heights(0, 0, 0, 3, 4, 0)))


# Дополнительные задачи: 1 (медиана), 2(впис.окружность), 3(опис.окружность)
# def leng(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     return sqrt((x_a - x_b)**2 + (y_a - y_b)**2)
#
# def side_ab(x_a: float, y_a: float, x_b: float, y_b: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     return AB
#
# def side_ac(x_a: float, y_a: float, x_c: float, y_c: float) -> float:
#     AC = leng(x_a, y_a, x_c, y_c)
#     return AC
#
# def side_bc(x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     BC = leng(x_b, y_b, x_c, y_c)
#     return BC
#
# print("Длины сторон треугольника ABC: ", side_ab(0, 0, 0, 3), side_ac(0, 0, 4, 0), side_bc(0, 3, 4, 0))
#
# def perim(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     return AB + AC + BC
# print("Периметр треугольника ABC: ", perim(0, 0, 0, 3, 4, 0))
#
# def area(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     return S
# print("Площадь треугольника ABC: ", area(0, 0, 0, 3, 4, 0))
#
# def median(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     m = sqrt((0.5 * AB ** 2) + (0.5 * AC ** 2) - (0.25 * BC ** 2))
#     return m
# print("Медиана треугольника ABC: ", (median(0, 0, 0, 3, 4, 0)))
#
# def r_inc(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     r = (2 * S) / (AB + AC + BC)
#     return r
# print("Радиус вписанной окружности треугольника ABC: ", r_inc(0, 0, 0, 3, 4, 0))
#
# def r_circ(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float) -> float:
#     AB = leng(x_a, y_a, x_b, y_b)
#     AC = leng(x_a, y_a, x_c, y_c)
#     BC = leng(x_b, y_b, x_c, y_c)
#     P = perim(x_a, y_a, x_b, y_b, x_c, y_c) / 2
#     S = sqrt(P * (P - AB) * (P - AC) * (P - BC))
#     R = (AB * AC * BC) / (4 * S)
#     return R
# print("Радиус описанной окружности треугольника ABC: ", r_circ(0, 0, 0, 3, 4, 0))
