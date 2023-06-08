#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]
    print("{} argument{}{}"
            .format(argc, 's' if argc != 1 else '', ':' if argc else '.'))
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
