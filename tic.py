import random


# Дъска за Морски шах
board = [' ' for _ in range(9)]
player_symbol = 'X'
computer_symbol = 'O'


def print_board(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")


def is_winner(board, symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]

    for combination in winning_combinations:
        if board[combination[0]] == symbol and board[combination[1]] == symbol and board[combination[2]] == symbol:
            return True
    return False


def is_board_full(board):
    return ' ' not in board


def evaluate(board):
    if is_winner(board, player_symbol):
        return -1
    elif is_winner(board, computer_symbol):
        return 1
    else:
        return 0


def minimax(board, depth, is_maximizing_player):
    if is_winner(board, player_symbol):
        return -1
    if is_winner(board, computer_symbol):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer_symbol
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player_symbol
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval


def get_best_move(board):
    best_eval = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer_symbol
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move


def play():
    print("Welcome to Tic Tac Toe!")
    print("You are playing as 'X'. The computer is 'O'.")
    print("Use the numbers 1-9 to place your move.")
    print_board(board)

    while not is_board_full(board):

        # Player's turn
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] != ' ' or player_move < 0 or player_move > 8:
            print("Invalid move. Try again.")
            continue

        board[player_move] = player_symbol
        print_board(board)

        if is_winner(board, player_symbol):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer is thinking...")
        computer_move = get_best_move(board)
        board[computer_move] = computer_symbol
        print_board(board)

        if is_winner(board, computer_symbol):
            print("Sorry, you lose.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

play()
