# Ex.38
# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user and then report the appropriate name as part
# of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
# If a number of sides outside this range is entered then your program should display an appropriate error message.
#
Number_of_sides = input("Enter the number of sides: ")
if Number_of_sides == "3":
    print('This is triangle or trigon (тругольник)')
elif Number_of_sides == "4":
    print('This is quadrilateral or tetragon (четырехугольник)')
elif Number_of_sides == "5":
    print('This is pentagon (пятиугольник)')
elif Number_of_sides == "6":
    print('This is hexagon (шестиугольник)')
elif Number_of_sides == "7":
    print('This is heptagon (семиугольник)')
elif Number_of_sides == "8":
    print('This is octagon (восьмиугольник)')
elif Number_of_sides == "9":
    print('This is nonagon, enneagon (девятиугольник)')
elif Number_of_sides == "10":
    print('This is decagon (десятиугольник)')
else: print('error')
#
# Ex.39
# The length of a month varies from 28 to 31 days. In this exercise you will create a program
# that reads the name of a month from the user as a string. Then your program should display
# the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

month = input("Enter the name of the month: ")
if month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print(f'{month} has 30 days')
elif month == 'February':
    print(f'{month} has 28 or 29 days')
else:
    print(f'{month} has 31 days')
#
# Ex.55
# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below: (photo).
# Write a program that reads a wavelength from the user and reports its color.
# Display an appropriate error message if the wavelength entered by the user is outside of the visible spectrum.
#
Nm = int(input("Enter the number of nanometers: "))
if Nm >= 380 and Nm < 450:
    print("The color of wavelength is violet")
elif Nm >= 450 and Nm < 495:
    print("The color of wavelength is blue")
elif Nm >= 495 and Nm < 570:
    print("The color of wavelength is green")
elif Nm >= 570 and Nm < 590:
    print("The color of wavelength is yellow")
elif Nm >= 590 and Nm < 620:
    print("The color of wavelength is orange")
elif Nm >= 620 and Nm < 750:
    print("The color of wavelength is red")
else:
    print("error")
#
# Ex.56
# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below: (photo). Write a program that reads the frequency
# of some radiation from the user and displays name of the radiation as part of an appropriate message.
#
Hz = float(input("Enter the frequency of radiation: "))
if Hz < 3e9:
    print("These are Radio Waves")
elif Hz >= 3e9 and Hz < 3e12:
    print("These are Microwaves")
elif Hz >= 3e12 and Hz < 4.3e14:
    print("This is Infrared Light")
elif Hz >= 4.3e14 and Hz < 7.5e14:
    print("This is Visible Light")
elif Hz >= 7.5e14 and Hz < 3e17:
    print("This is Ultraviolet Light")
elif Hz >= 3e17 and Hz < 3e19:
    print("These are X-Rays")
elif Hz >= 3e19:
    print("These are Gamma Rays")
else:
    print("error")
#
# Ex.58
# Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually
# slightly more than that. As a result, an extra day, February 29, is included in some years to correct
# for this difference. Such years are referred to as leap years. The rules for determining whether or not
# a year is a leap year follow:
# • Any year that is divisible by 400 is a leap year.
# • Of the remaining years, any year that is divisible by 100 is not a leap year.
# • Of the remaining years, any year that is divisible by 4 is a leap year.
# • All other years are not leap years.
# Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.
#
year = int(input("Enter the year: "))
if year % 400 == 0 or year % 4 == 0:
    print("This is Leap Year")
elif year % 100 == 0:
    print("This is not a Leap Year")
else:
    print("This is not a Leap Year")
