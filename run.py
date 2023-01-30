# tic Tac Toe game

print("Hello!  :)")
user = input("Whats your name?\n")
print("-----------------------------------------")
print(f"Hi {user}, lets play a game of Tic Tac Toe against me.\n")
print("I bet that even if you are extremely intelligent I can beat you.\n")
print("-----------------------------------------")
print("Each position on the board has a number equivalent")
print("to the position you want to place your move.\n")
print("The board starts at position 1 in the top left corner")
print("and ends at position 9 in the bottom right corner.\n")
print("You just need to select a position from number 1 to number 9, press")
print("enter and the postion that you want will be marked on the board\n")
print("Now that you know how the game works, do you your best to beat me")
print("-----------------------------------------")


def show_board(board):

    """
    Function to display the game board
    """
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---+---+---")
    print(" {} | {} | {} \n".format(board[7], board[8], board[9]))


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

    """
    Function of game draw condition
    """
    for i in range(1, len(board)):
        if board[i] == " ":
            return False
    if not victory(board, "X") and not victory(board, "O"):
        return True
    else:
        return False


def play_game():

    """
    Function to start the game
    Posses the game loops, so the user can decide to restart the game or not
    """
    moves = 0
    board = [" " for x in range(10)]
    while True:
        # input number equivalent to the position on the board
        show_board(board)
        user_m = input("Enter a move from 1 to 9: \n")
        if user_m.isnumeric() and int(user_m) > 0 and int(user_m) < 10:
            user_m = int((user_m))
            if board[user_m] == " ":
                board[user_m] = "X"
                moves += 1
            else:
                print("----------------------------------------------------")
                print("Invalid move. Please enter a number between 1 and 9.")
                print("----------------------------------------------------")
                continue
        else:
            print("----------------------------------------------------")
            print("Invalid move. Please enter a number between 1 and 9.")
            print("----------------------------------------------------")
            continue
        # user victory conditions with frases to interact with user
        if victory(board, "X"):
            print("----------------------------------------------------------")
            print(f"You won {user}! Congratulations")
            play_again = input(f"{user} Do you like to play again? (yes/no)\n")
            print("----------------------------------------------------------")
            if play_again.lower() == 'no':
                print("-------------------------------")
                print(f"See you later {user}")
                print("It was nice to play against you")
                print("-------------------------------")
                break
            elif play_again.lower() == 'yes':
                print("-----------------------")
                print(f"One more round {user}!")
                print("-----------------------")
                return play_game()
        # draw condition
        elif its_a_draw(board):
            print("------------------------------------------------------")
            print(f"Its a draw {user}")
            play_again = input(f"{user} Do you like to play again? (yes/no)\n")
            print("------------------------------------------------------")
            if play_again.lower() == 'no':
                print("-------------------------------")
                print(f"See you later {user}\n")
                print("It was nice to play against you")
                print("-------------------------------")
                break
            elif play_again.lower() == 'yes':
                print("-----------------------")
                print(f"One more round {user}!")
                print("-----------------------")
                return play_game()
        ai_turn(board)
        # AI victory conditions with frases to interact with user
        if victory(board, "O"):
            print("----------------------------------------------------------")
            print(f"You Lost {user}! I was far superior then you. Hahahaha!\n")
            play_again = input(f"{user} Do you like to play again? (yes/no)\n")
            print("----------------------------------------------------------")
            if play_again.lower() == 'no':
                print("-------------------------------")
                print(f"See you later {user}\n")
                print("It was nice to play against you")
                print("-------------------------------")
                break
            elif play_again.lower() == 'yes':
                print("-----------------------")
                print(f"One more round {user}!")
                print("-----------------------")
                return play_game()
        # draw condition
        elif its_a_draw(board):
            print("------------------------------------------------------")
            print(f"Its a draw {user}")
            play_again = input(f"{user} Do you like to play again? (yes/no)\n")
            print("------------------------------------------------------")
            if play_again.lower() == 'no':
                print("-------------------------------")
                print(f"See you later {user}\n")
                print("It was nice to play against you")
                print("-------------------------------")
                break
            elif play_again.lower() == 'yes':
                print("-----------------------")
                print(f"One more round {user}!")
                print("-----------------------")
                return play_game()
        

play_game()