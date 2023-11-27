board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
game_on = True


def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def adding_values(p, c):
    if board[c - 1] != "_":
        print("!!! Alert !!!")
        c = int(input("That Column is occupied.Pick another column:"))
        adding_values(p, c)
    if p == "player 1":
        board[c - 1] = "X"
    else:
        board[c - 1] = "O"


def check_results():
    global game_on
    if count == 10:
        game_on = False
        print("Game is a draw!!")
    else:
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                                [0, 4, 8], [2, 4, 6]]  # Diagonal

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == "X":
                game_on = False
                print("*****************WINNER********************")
                print("Player 1 Won the game! Congratulations.")
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == "O":
                game_on = False
                print("******************WINNER*******************")
                print("Player 2 Won the game! Congratulations.")


print("Welcome to Tic Tac Toe!")
print("player 1 will be 'X' and player 2 will be 'O'.")
print("every column is represented by 1-9. Use number 1 - 9 to tell which column u want to use.")
print_board()
count = 1
while game_on:
    if count % 2 == 0:
        player = "player 2"
    else:
        player = "player 1"
    choice = int(input(f"Its {player} turn. Please pick a column:"))
    adding_values(player, choice)
    print_board()
    count += 1
    check_results()
