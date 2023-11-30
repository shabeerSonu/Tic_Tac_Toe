import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                        [0, 4, 8], [2, 4, 6]]  # Diagonal
game_on = True


print("Welcome to Tic Tac Toe!")
print("_______________________")
print("player 1 will be 'X' and player 2 will be 'O'.")
print("every column is represented by 1-9. Use number 1 - 9 to tell which column you want to use.")
print("Which game mode would you like to play")
game_mode = input("Type '1' for one player and '2' for two player:")


# **************** Functions *****************

# function to print the board
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


# checking if computer can win the game in next move
def computer_winning_move():
    players_list = ["O", "X"]
    for p in players_list:
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == p:
                if board[combo[2]] == "_":
                    return combo[2]
            elif board[combo[1]] == board[combo[2]] == p:
                if board[combo[0]] == "_":
                    return combo[0]
            elif board[combo[0]] == board[combo[2]] == p:
                if board[combo[1]] == "_":
                    return combo[1]
    return None


def computer_turn():
    winning_move = computer_winning_move()
    if winning_move is not None:
        print(winning_move)
        board[winning_move] = "O"
    elif board[4] == "_":
        board[4] = "O"
    else:
        empty_cell = [i for i in range(0,8) if board[i] == "_" ]
        if empty_cell:
            random_cell = random.choice(empty_cell)
            board[random_cell] = "O"


# adding user input to the board
def adding_values(p, c):
    if board[c - 1] != "_":
        print("!!! Alert !!!")
        c = int(input("That Column is occupied.Pick another column:"))
        adding_values(p, c)
    board[c - 1] = p


# Checking if anyone has won
def check_results(p):
    global game_on

    for combo in winning_combinations:
        # checking if anyone won the game
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == p:
            game_on = False
            print("***************** WINNER ********************")
            if game_mode == "1":
                player2 = "Computer"
            else:
                player2 = "Player 2"
            print(f"{'player 1' if p =='X' else player2} Won the game! Congratulations.")
            print_board()
    # checking if the game is draw or not.
    if all(cell == "X" or cell == "O" for cell in board) and game_on:
        game_on = False
        print("******** DRAW **********")
        print("Game is a draw!!")


# *******************************************************

count = 1
if game_mode == "1":
    while game_on:
        print_board()
        choice = int(input("Its players turn. Please pick a column:"))
        adding_values("X", choice)
        check_results("X")
        computer_turn()
        check_results("O")

else:
    print_board()
    while game_on:
        # deciding whose turn is to play
        if count % 2 == 0:
            player = "O"
        else:
            player = "X"

        # taking user input
        choice = int(input(f"Its {'player 1' if player =='X' else 'player 2'} turn. Please pick a column:"))
        adding_values(player, choice)
        print_board()
        check_results(player)
        count += 1

