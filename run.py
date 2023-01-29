# tic Tac Toe game

player = input("Hey YOU!!! Whats your name?\n")

player_answer = input(f"Hi {player}, do you want to play a game of Tic Tac Toe against me?\n")

#function not working / find out why
def show_board(board):
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))
    print("---+---+---")
    