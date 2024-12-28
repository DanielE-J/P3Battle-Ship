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

