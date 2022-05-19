from .board import *
from .checkDraw import *
from .checkWin import *
from .constants import *
from .endGame import *
from .play import *
from .playAgain import *
from .playerOneMove import *
from .playerTwoMove import *


def endGame(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True
