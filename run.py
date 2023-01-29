# tic Tac Toe game

user = input("Hey YOU!!! Whats your name?\n")

print(f"Hi {user}, lets play a game of Tic Tac Toe against me. \n")
print("I bet that even brilliant the way u r I can beat you\n")


def show_board(board):

    """
    Function to display the game board
    """
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))


def victory(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
       (board[4] == player and board[5] == player and board[6] == player) or \
       (board[7] == player and board[8] == player and board[9] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[3] == player and board[6] == player and board[9] == player) or \
       (board[1] == player and board[5] == player and board[9] == player) or \
       (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False       


def play_game():
    board = [" " for x in range(10)]
    while True:
        # input number equivalent to the position on the board
        show_board(board)
        user_move = int(input("Enter your move (1-9): \n"))
        if board[user_move] == " ":
            board[user_move] = "X"
        else:
            # check if input the same number
            print("Invalid move. Try again.")
            continue
        if victory(board, "X"):
            print(f"You won {user}! Congratulations")
            play_again = input(f"{user} would you like to play again? (yes/no)\n")
            if play_again.lower() == 'no':
                print(f"See you later {user}\n")
                break
            elif play_again.lower() == 'yes':
                print(f"One more round {user}")
                return play_game()


play_game()