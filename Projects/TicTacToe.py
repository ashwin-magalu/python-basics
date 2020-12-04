"""
Board
Display Board
Play Game
Handle Turn
Check Win
    Chech Rows, Columns and Diagonals
Check Tie
Flip Player
"""


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_still_going = True
current_player = "Player X"
winner = None


def play_game():
    display_board()  # display the initial board first
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "Player X" or winner == "Player O":
        print("Winner: " + winner)
    elif winner == None:
        print("This match is a tie")


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):
    position = input(player + "'s turn.Choose a position from 1-9: ")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ]:
            position = input(
                player + "'s turn. Invalid Input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't choose that block, as it is already taken")

    if player == "Player X":
        board[position] = 'X'
    elif player == "Player O":
        board[position] = "O"
    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return "Player "+board[0]
    elif row_2:
        return "Player "+board[3]
    elif row_3:
        return "Player "+board[6]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return "Player "+board[0]
    elif column_2:
        return "Player "+board[1]
    elif column_3:
        return "Player "+board[2]
    return


def check_diagonals():
    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_still_going = False

    if diag_1:
        return "Player "+board[0]
    elif diag_2:
        return "Player "+board[2]
    return


def check_for_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "Player X":
        current_player = "Player O"
    elif current_player == "Player O":
        current_player = "Player X"


play_game()
