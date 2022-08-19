# Letter Grade Points
# A+ 4.0
# A 4.0
# A- 3.7
# B+ 3.3
# B 3.0
# B- 2.7
# C+ 2.3
# C 2.0
# C- 1.7
# D+ 1.3
# D 1.0
# F 0

# summ = 0
# count = 0
#
# mark = input("Введите оценку: ")
#
# if mark == 'A+':
#     summ = summ + 4.0
# elif mark == 'A':
#     summ = summ + 4.0
# elif mark == 'A-':
#     summ = summ + 3.7
# elif mark == 'B+':
#     summ = summ + 3.3
#
# count = count + 1
#
# mark = input()
#
# while mark != '':
#     if mark == 'A+':
#         summ = summ + 4.0
#     elif mark == 'A':
#         summ = summ + 4.0
#     elif mark == 'A-':
#         summ = summ + 3.7
#     elif mark == 'B+':
#         summ = summ + 3.3
#
#     count = count + 1
#
#     mark = input()
#
# average = summ / count
# print(f'Средняя оценка: {average}')


# When this algorithm completes, guess contains an approximation of the square
# root of x. The quality of the approximation depends on how you define “good
# enough”. In the author’s solution, guess was considered good enough when the
# absolute value of the difference between guess ∗ guess and x was less than or equal
# to 10e−12.

# |2| = 2
# |-2| = 2
# |3| = 3


# 10e-12 = 10 * 10^(-12) = 10^(-11)
# 1e-12

# x = float(input())
# guess = x / 2
# print(guess)
# while abs(guess * guess - x) > 1e-12:
#     average = (guess + x/guess) / 2
#     guess = average
#     print(guess)

# import math
# x = math.sqrt(x)


# def example_function():
#     pass
#     pass
#     return None

# input(), int(), print()
# input - return (str)

# def avg(a, b):
#     average = (a + b) / 2
#     return average
#
#
# print(avg(1, 3))
# print(avg(1, 1000))

# Ex 85
# Write a function that takes the lengths of the two shorter sides of a right triangle as
# its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
# theorem, as the function’s result. Include a main program that reads the lengths of
# the shorter sides of a right triangle from the user, uses your function to compute the
# length of the hypotenuse, and displays the result

# def sqrt(x):
#     guess = x / 2
#     while abs(guess * guess - x) > 1e-12:
#         average = (guess + x / guess) / 2
#         guess = average
#     return guess
#
#
# def hyp(a, b):
#     c = sqrt(a ** 2 + b ** 2)
#     return c

# a = float(input('The first side'))
# b = float(input('The second side'))
# c = hyp(a, b)
#
# print(f'Hypotenuse is {c}')


# f-string - format

# a^2 + b^2 = c^2
# c = sqrt(a^2 + b^2)

# Exercise 94: Is It a Valid Triangle?
# If you have 3 straws, possibly of differing lengths, it may or may not be possible
# to lay them down so that they form a triangle when their ends are touching. For
# example, if all of the straws have a length of 6 inches then one can easily construct
# an equilateral triangle using them. However, if one straw is 6 inches long, while
# the other two are each only 2 inches long, then a triangle cannot be formed. More
# generally, if any one length is greater than or equal to the sum of the other two then
# the lengths cannot be used to form a triangle. Otherwise they can form a triangle.
# Write a function that determines whether or not three lengths can form a triangle.
# The function will take 3 parameters and return a Boolean result. If any of the lengths
# are less than or equal to 0 then your function should return False. Otherwise it
# should determine whether or not the lengths can be used to form a triangle using
# the method described in the previous paragraph, and return the appropriate result.
# In addition, write a program that reads 3 lengths from the user and demonstrates the
# behaviour of your function.


# Type hinting: подсказка по типап
def is_valid(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True


print(is_valid(3, 4, 5)) # True
print(is_valid(10, 4, 5)) # False
print(is_valid(-3, 4, -1)) # False
print(is_valid(3, 4, 2)) # True

print(is_valid(10, 4, 5))