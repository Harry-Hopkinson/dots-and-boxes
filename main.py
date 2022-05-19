from lib.checkDraw import *
from lib.checkWin import *
from lib.constants import *
from lib.endGame import *
from lib.play import *
from lib.playAgain import *
from lib.playerOneMove import *
from lib.playerTwoMove import *
from lib.board import *
from lib.printBoard import *

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
