from board import *
from checkDraw import *
from checkWin import *
from constants import *
from endGame import *
from play import *
from playAgain import *
from playerOneMove import *
from playerTwoMove import *

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

running = True

while running:
    printBoard(board)
    if playerOneMove(board):
        running = False
    if playerTwoMove(board):
        running = False

playAgain()

print("Thanks for playing!")
