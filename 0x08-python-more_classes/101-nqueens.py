#!/usr/bin/python3

"""solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard"""
    my_board = []
    [my_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in my_board]
    return (my_board)


def board_deepcopy(my_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(my_board, list):
        return list(map(board_deepcopy, my_board))
    return (my_board)

def get_solution(my_board):
    """Return the list representation of a solved chessboard."""
    solution = []
    for r in range(len(my_board)):
        for c in range(len(my_board)):
            if my_board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(my_board, row, col):
    """X out spots on a chessboard"""

    for j in range(col + 1, len(my_board)):
        my_board[row][j] = "x"

    for j in range(col - 1, -1, -1):
        my_board[row][j] = "x"

    for k in range(row + 1, len(my_board)):
        my_board[k][col] = "x"
    
    for k in range(row - 1, -1, -1):
        my_board[k][col] = "x"
    
    j = col + 1
    for k in range(row + 1, len(my_board)):
        if j >= len(my_board):
            break
        my_board[k][j] = "x"
        j += 1

    j = col - 1

    for k in range(row - 1, -1, -1):
        if j < 0:
            break
        my_board[k][j]
        j -= 1

    for k in range(row - 1, -1, -1):
        if j >= len(my_board):
            break
        my_board[k][j] = "x"
        j += 1

    j = col - 1
    for k in range(row + 1, len(my_board)):
        if j < 0:
            break
        my_board[k][j] = "x"
        j -= 1


def recursive_solve(my_board, row, queens, solutions):
    """Recursively solve an N-queens puzzle"""

    if queens == len(my_board):
        solutions.append(get_solution(my_board))
        return (solutions)

    for j in range(len(my_board)):
        if my_board[row][j] == " ":
            tmp_board = board_deepcopy(my_board)
            tmp_board[row][j] = "Q"
            xout(tmp_board, row, j)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    my_board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(my_board, 0, 0, [])
    for sol in solutions:
        print(sol)
