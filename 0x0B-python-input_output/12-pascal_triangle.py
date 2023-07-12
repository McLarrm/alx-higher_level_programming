#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return []
    n -= 1
    for row in range(n + 1):
        triangle.append([])
        triangle[row].append(1)
        for col in range(int(row / 2)):
            triangle[row].append(triangle[row - 1][col] +
                                 triangle[row - 1][col + 1])
        if row % 2 == 1:
            triangle[row].extend(triangle[row][::-1])
        else:
            triangle[row].extend(triangle[row][-2::-1])
    return triangle
