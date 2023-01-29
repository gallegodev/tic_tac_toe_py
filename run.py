"""
To do list:
- Fix bugs  if user puts numbers or letters on input
- its_a_draw functions needs to be fix / draw is not happening

"""




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

    """
    Gives the condition for victory of the game
    """
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


def ai_turn(board):

    """
    Gives the computer move on the board after the user move
    """
    import random
    while True:
        move = random.randint(1, 9)
        if board[move] == " ":
            board[move] = "O"
            break


def its_a_draw(board):
    if " " not in board:
        return True
    else:
        return False


def play_game():

    """
    Function to start the game
    Posses the game loops, so the user can decide to restart the game or not
    """
    board = [" " for x in range(10)]
    while True:
        # input number equivalent to the position on the board
        show_board(board)
        user_move = int(input("Enter your move (1-9): \n"))
        if user_move < 1 or user_move > 9:
            print("Invalid move. Please enter a number between 1 and 9.")
            continue
        if board[user_move] == " ":
            board[user_move] = "X"
        else:
            # check if user input the same number
            print("Invalid move. Try again.")
            continue
        # user victory conditions with frases to interact with user
        if victory(board, "X"):
            print(f"You won {user}! Congratulations")
            play_again = input(f"{user} Do you like to play again? (yes/no)\n")
            if play_again.lower() == 'no':
                print(f"See you later {user}\n")
                break
            elif play_again.lower() == 'yes':
                print(f"One more round {user}")
                return play_game()
       
        ai_turn(board)
        # ai victory conditions with frases to interact with user
        if victory(board, "O"):
            print(f"You Lost {user}! I was far superior then you. Hahahaha!\n")
            play_again = input(f"{user} Do you like to play again? (yes/no)\n")
            if play_again.lower() == 'no':
                print(f"See you later {user}\n")
                break
            elif play_again.lower() == 'yes':
                print(f"One more round {user}")
                return play_game()
        its_a_draw(board)
        if its_a_draw(board):
            print("Its a draw my worthy adversary!")
            break


play_game()