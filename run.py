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

"""
Function to place ships randomly on the board
"""
def place_ships(board):
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    for ship, size in ships.items():
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, 8)
                col = random.randint(0, 9 - size)
                if all(board[row][col+i] == ' ' for i in range(size)):
                    for i in range(size):
                        board[row][col+i] = 'O'
                    placed = True
            else:
                row = random.randint(0, 9 - size)
                col = random.randint(0, 8)
                if all(board[row+i][col] == ' ' for i in range(size)):
                    for i in range(size):
                        board[row+i][col] = 'O'
                    placed = True        