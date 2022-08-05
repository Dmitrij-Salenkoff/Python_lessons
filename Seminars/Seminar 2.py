import math

# imports
# f-strings
# .split() and methods
# 1e10 == 1 * 10 ** 10
# booleans
# if-statements

# a = 10
# b = 2
# print(f"Произведение равно: {a*b} \nЧастное равно: {a/b}\nСумма равна: {a+b}\nРазность равна: {a-b}")

# a = int(input())
# b = input()

# a, b, c, d, e = map(float, input().split())
# # "10 2" -> "10" "2"
# print(a, b, c, d, e)

# # a = 64000000000000000
# a = 64e15 # = 64 * (10 ** 15)
# # b = 0.000004
# b = 4e-6 # = 4 * (10 ** -6)


# id-elif-else statements


# Ex 35
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.

# a = int(input())
#
# if a % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")


# Ex 37
# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.

# letter = input()

# 1 method
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print(f'Letter {letter} is a vowel')
# elif letter == 'y':
#     print(f'Letter {letter} is a vowel or consonant')
# else:
#     print(f'Letter {letter} is a consonant')

# 2 method
# if letter in ['a', 'e', 'i', 'o', 'u']:
#     print(f'Letter {letter} is a vowel')
# elif letter == 'y':
#     print(f'Letter {letter} is a vowel or consonant')
# else:
#     print(f'Letter {letter} is a consonant')

# Ex 41
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
# scalene. All three sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of the three sides of a triangle from the
# user. Then display a message that states the triangle’s type.

# a, b, c = map(float, input().split())
# if a == b and b == c:
#     print('The triangle is equilateral')
# elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
#     print("The triangle is isosceles")
# else:
#     print("Triangle is scalene")


# # Ex 49
# # 2002 Horse
# # 2003 Sheep
# # 2004 Monkey
# # 2005 Rooster
# # 2006 Dog
# # 2007 Pig
# # 2008 Rat
# # 2009 Ox
# # 2010 Tiger
# # 2011 Hare
# year = int(input())
#
# if year % 12 == 8:
#     print("Dragon")
# elif year % 12 == 9:
#     print("Snake")
# elif year % 12 == 10:
#     print("Horse")
# elif year % 12 == 11:
#     print("Sheep")
# elif year % 12 == 0:
#     print("Monkey")
# elif year % 12 == 1:
#     print("Rooster")
# elif year % 12 == 2:
#     print("Dog")
# elif year % 12 == 3:
#     print("Pig")
# elif year % 12 == 4:
#     print("Rat")
# elif year % 12 == 5:
#     print("Ox")
# elif year % 12 == 6:
#     print("Tiger")
# elif year % 12 == 7:
#     print("Hare")


# Ex 51
# Write a program that computes the real roots of a quadratic function.
# Your program should begin by prompting the user for the values of a, b and c. Then it should
# display a message indicating the number of real roots, along with the values of the
# real roots (if any).

a, b, c = map(float, input().split())

D = b ** 2 - 4 * a * c  # Дискриминант

if D < 0:
    print("There are no roots")
elif D == 0:
    root = -b / (2 * a)
    print(f'The root is {root}')
else:
    root_1 = (-b + math.sqrt(D)) / (2 * a)
    root_2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'The roots are {root_1} and {root_2}')
