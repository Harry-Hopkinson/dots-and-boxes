from board import *
from checkDraw import *
from checkWin import *
from constants import *
from endGame import *
from play import *
from playAgain import *
from playerOneMove import *
from playerTwoMove import *
from main import board
from board import resetBoard

playAgain = input("Play again? (y/n): ")
if playAgain == "y":
    resetBoard(board)
    running = True
