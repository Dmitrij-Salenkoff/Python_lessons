#Ex.2
# Write a program that asks the user to enter his or her name.
# The program should respond with a message that says hello to the user, using his or her name.
name = input("Enter the name: ")
print("Hello,", name)

#Ex.4
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
length = float(input("Enter the length (in feet): "))
width = float(input("Enter the width (in feet): "))
area = length * width / 43560
print(area, "acres")

#Ex.10
#Create a program that reads two integers, a and b, from the user.
#The sum of a and b
# The difference when b is subtracted from a
# The product of a and b
# The quotient when a is divided by b
# The remainder when a is divided by b
# The result of log10 a
# The result of ab
a = 6
b = 2
print("Summ of a and b = ", (a + b))
print("The difference when b is subtracted from a = ", a - b)
print("The product of a and b = ", a * b)
print("The quotient when a is divided by b = ", int(a / b))
print("The remainder when a is divided by b = ", a % b)
import math
print("The result of log10 a = ", math.log10(a))
print("The result of ab = ", a ** b)
