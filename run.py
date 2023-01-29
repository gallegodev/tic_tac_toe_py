# tic Tac Toe game

player = input("Hey YOU!!! Whats your name?\n")

print(f"Hi {player}, lets play a game of Tic Tac Toe against me. \n")
print("I bet that even brilliant the way u r I can beat you")


def show_board(board):
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))


def play_game():
    board = [" " for x in range(10)]
    while True:
        show_board(board)
        user_move = int(input("Enter your move (1-9): "))
        if board[user_move] == " ":
            board[user_move] = "X"
        else:
            print("Invalid move. Try again.")
            continue

play_game()