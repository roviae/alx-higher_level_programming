#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = " and is greater than 5"
str2 = " and is 0"
str3 = " and is less than 6 and not 0"
str4 = "Last digit of "
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print(f"{}  {} is {} {}".format(str4, number, lastdigit, str1))
elif lastdigit == 0:
    print(f"{} {} is {} {}".format(str4, number, lastdigit, str2))
else:
    print(f"{} {} is {} {}".format(str4, number, lastdigit, str3))
