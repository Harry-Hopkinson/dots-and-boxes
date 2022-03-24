from board import *
from checkDraw import *
from checkWin import *
from constants import *
from endGame import *
from play import *
from playAgain import *
from playerOneMove import *
from playerTwoMove import *
from printBoard import *


def playerOneMove(board):
    while True:
        i = int(input("Enter row: "))
        j = int(input("Enter column: "))
        if play(board, 1, i, j):
            break
        else:
            print("Invalid move")
    printBoard(board)
    if checkWin(board, 1):
        print("Player 1 wins")
        printBoard(board)
        return True
    elif checkDraw(board):
        print("Draw")
        return True
    else:
        return False
