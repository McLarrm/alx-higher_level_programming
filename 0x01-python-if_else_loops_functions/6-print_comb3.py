#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        print("{:d}{:d}".format(num1, num2), end="")
        if (int(str(num1) + str(num2)) < 89):
            print(", ", end="")
print("\n")
