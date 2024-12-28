import random
"""
Created an empty board
"""

def create_board():
    board = []
    for _ in range(10):
        row = [' '] * 10
        board.append(row)
    return board

"""
Function to print the board
"""

def print_board(board):
    print('   A B C D E F G H I J')
    print('  -------------------')
    for i in range(10):
        print(f'{j+1} |{"|".join(board[j])}|')
        print('  -------------------')