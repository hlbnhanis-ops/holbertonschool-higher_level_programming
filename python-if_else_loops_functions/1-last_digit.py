#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of " + str(number) + " is " + str(number % 10), end="")
if number > 5:
    print(" and is greater than 5\n")
elif number == 0:
    print(" and is 0\n")
else:
    print(" and is less than 6 and not 0\n")
