from checkDraw import *
from checkWin import *
from constants import *
from endGame import *
from play import *
from playAgain import *
from playerOneMove import *
from playerTwoMove import *
from board import *


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print(".", end="")
            elif board[i][j] == 1:
                print("x", end="")
            elif board[i][j] == -1:
                print("o", end="")
        print()
    print(hash)
