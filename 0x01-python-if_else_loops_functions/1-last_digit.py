#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Digit = abs(number) % 10
if number < 0:
    Digit = -Digit
print(f"Last digit of {number} is {Digit} and is ", end="")
if Digit > 5:
    print("greater than 5")
elif Digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
