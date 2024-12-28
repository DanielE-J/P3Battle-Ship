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
                row = random.randint(0, 9)
                col = random.randint(0, 10 - size)
                if all(board[row][col+j] == ' ' for j in range(size)):
                    for j in range(size):
                        board[row][col+j] = 'O'
                    placed = True
            else:
                row = random.randint(0, 10 - size)
                col = random.randint(0, 9)
                if all(board[row+j][col] == ' ' for j in range(size)):
                    for j in range(size):
                        board[row+j][col] = 'O'
                    placed = True

"""
Allows the user to place ships manually on the board.
"""                           
def place_ships_manually(board, board_size=10):
 
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    
    for ship, size in ships.items():
        placed = False
        while not placed:
            print(f"\nPlacing the {ship} (size {size})")
            print_board(board)
            
            # Get user input for orientation
            orientation = input("Enter orientation (horizontal/vertical): ").strip().lower()
            if orientation not in ['horizontal', 'vertical']:
                print("Invalid orientation! Please enter 'horizontal' or 'vertical'.")
                continue
            
            # Get user input for starting position
            try:
                row = int(input("Enter starting row (0-9): "))
                col = int(input("Enter starting column (0-9): "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            
            # Validate position and fit
            if orientation == 'horizontal':
                if col + size > board_size or any(board[row][col + j] != ' ' for j in range(size)):
                    print("Invalid position or overlap! Try again.")
                    continue
                # Place the ship
                for j in range(size):
                    board[row][col + j] = 'O'
                placed = True
            else:  # Vertical
                if row + size > board_size or any(board[row + j][col] != ' ' for j in range(size)):
                    print("Invalid position or overlap! Try again.")
                    continue
                # Place the ship
                for j in range(size):
                    board[row + j][col] = 'O'
                placed = True

    print("\nFinal Board:")
    print_board(board)