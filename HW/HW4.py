# # Задачник старый: задачи 86, 88
# # Задачник Абрамяна: For7, For17 (c 20й страницы), Proc20 (с 31й страницы)
#
# # 86
# # In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# # Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# # as its only result. Write a main program that demonstrates the function.
#
base_fare = 4.00 # основной тариф
plus_base_fare = 0.25 # добавляется за каждые 140м (0.14км)
def taxi_fare(distance_km): # вводить будем расстояние в км
    price_for_plus_base_fare = (distance_km / 140) * 1000 # получается сумма (каждые 140m), на которую надо умножить 0.25
    total_fare = base_fare + (plus_base_fare * price_for_plus_base_fare)
    return total_fare
print(taxi_fare(0.56))
print(taxi_fare(2.8))
print(taxi_fare(9.1))
#
# # 88
# # Write a function that takes three numbers as parameters, and returns the median value of those parameters
# # as its result. Include a main program that reads three values from the user and displays their median.
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

def median(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    elif b < a and a < c or b > a and a > c:
        return a
    elif c < a and b < c or c > a and b > c:
        return c
    else:
        raise TypeError

print(median(a, b, c))
#
# # For7
# # Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.
a = int(input("Введите число: "))
b = int(input("Введите число: "))
# rnage(2, 10+1) - [2, 3, 4, 5, 6, 7, 8, 9, 10]; sum = 44
summ = 0
for i in range(a, b+1):
    summ = summ + i
print(summ)
#
# # For 17
# Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму 1+A+A**2 +A**3 +...+A**N.
1 = A ** 0
A = 0.5, N = 1000
summ = 1 + 0.5 + 0.25 + 0.125 + 0..... ~ 2
A = float(input("Введите число A: "))
N = int(input("Введите число N: "))
summ = 0
# range(N) - [0, 1, 2, 3, 4, ..., N-1]
for i in range(N+1):
    summ = summ + A ** i
print(f"Сумма равна: {summ}")
#
# # Proc20
# # Описать процедуру PowerA234(A, B, C, D), вычисляющую вторую, третью и четвертую степень числа A и возвращающую
# # эти степени соответственно в переменных B, C и D (A — входной, B, C, D — выходные параметры; все параметры являются
# # вещественными). С помощью этой процедуры найти вторую, третью и четвертую степень пяти данных чисел.
A = float(input("Введите число А: "))

def pow(A):
    B = A**2
    C = A**3
    D = A**4
    return B, C, D

# Proc20
# Описать процедуру PowerA234(A, B, C, D), вычисляющую вторую, третью и четвертую степень числа A и возвращающую
# эти степени соответственно в переменных B, C и D (A — входной, B, C, D — выходные параметры; все параметры являются
# вещественными). С помощью этой процедуры найти вторую, третью и четвертую степень пяти данных чисел.
A = float(input("Введите число А: "))
B = A**2
C = A**3
D = A**4
print("Вторая степень B:", B**2, "\n", "Третья степень В:", B**3, ";", "Четвертая степень B:", B**4, ";", "Пятая степень B:", B**5)
print("Вторая степень C:", C**2, ";", "Третья степень C:", C**3, ";", "Четвертая степень C:", C**4, ";", "Пятая степень C:", C**5)
print("Вторая степень D:", D**2, ";", "Третья степень D:", D**3, ";", "Четвертая степень D:", D**4, ";", "Пятая степень D:", D**5)
