from checkDraw import *
from checkWin import *
from constants import *
from endGame import *
from play import *
from playAgain import *
from playerOneMove import *
from playerTwoMove import *
from board import *
from printBoard import *

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

while True:
    printBoard(board)
    if playerOneMove(board):
        break
    if playerTwoMove(board):
        break

print("Thanks for playing!")
