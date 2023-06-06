#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
comparison = "greater than 5" if last_digit > 5 else "less than 6 and not 0" if last_digit < 6 else "0"
print("Last digit of", number, "is", last_digit, "and is", comparison)
