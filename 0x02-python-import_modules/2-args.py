#!/usr/bin/python3
import sys

print("{} argument{}{}".format(len(sys.argv) - 1, 's' if len(sys.argv) != 2 else '', ':' if len(sys.argv) > 1 else '.'), end='\n' if len(sys.argv) > 1 else '')

for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))
