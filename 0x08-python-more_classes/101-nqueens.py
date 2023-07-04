#!/usr/bin/python3
"""
Fuctions that searches for solutions to N-queen problems
"""


import sys


def is_safe(board, row, col, N):
    """ Check if a queen can be placed at board[row][col] """
    """ Check the left side of the row """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """ Check the upper diagonal on the left side """
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """ Check the lower diagonal on the left side """
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, N):
    """ Base case: If all queens are placed, print the solution """
    if col >= N:
        print_solution(board, N)
        return True

    """ Recursive case: Try placing a queen in each row of the current column """
    for i in range(N):
        if is_safe(board, i, col, N):
            """ Place the queen """
            board[i][col] = 1

            """ Recursive call to place queens in the next column """
            solve_nqueens(board, col + 1, N)

            """ Backtrack: Remove the queen from the current position """
            board[i][col] = 0

    return False


def print_solution(board, N):
    """ Print the board configuration """
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print(f"{i}, {j}", end="")
                if i != N - 1:
                    print(", ", end="")
    print()


def nqueens(N):
    """ Check if N is a valid integer """
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """ Check if N is at least 4 """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """ Create an empty board """
    board = [[0 for _ in range(N)] for _ in range(N)]

    """ Solve the N-queens problem """
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    """ Check the number of arguments """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """ Solve the N-queens problem """
    nqueens(sys.argv[1])
