import random
def display_menu():
    print("Welcome to Tic Tac Toe!")
    print("Menu:")
    print("1. Single Player (against CPU)")
    print("2. Dual Player")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return int(choice)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(cell == player for cell in [self.board[0][i], self.board[1][i], self.board[2][i]]):
            return player
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return player
    return None

def computer_move(board):
    # Simple strategy: try to block the opponent, then try to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_winner(board, 'O'):
                    return (i, j)
                board[i][j] = ' '

    # If no winning move, try to block a potential win
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_winner(board, 'X'):
                    return (i, j)
                board[i][j] = ' '

    # If no blocking move, take the center
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and (i == 1 and j == 1):
                return (i, j)

    # Random move
    from random import randint
    while True:
        i = randint(0, 2)
        j = randint(0, 2)
        if board[i][j] == ' ':
            break

    return (i, j)

def single_player():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Your turn. Enter a move (row and column): ")
        try:
            row, col = map(int, input().split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    break
                elif all(' ' not in row for row in board):
                    print("It's a draw!")
                    break

                ai_move = computer_move(board)
                board[ai_move[0]][ai_move[1]] = current_player
                if check_winner(board, current_player):
                    print(f"Computer wins!")
                    break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter valid row and column numbers.")

def run_game():
    while True:
        choice = display_menu()
        if choice == 1:
            single_player()
        elif choice == 2:
            # Dual player mode can be implemented similarly
            pass
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

run_game()
