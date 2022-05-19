from .board import *
from .checkDraw import *
from .checkWin import *
from .constants import *
from .endGame import *
from .play import *
from .playAgain import *
from .playerOneMove import *
from .playerTwoMove import *


def checkWin(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                if i + 3 < len(board):
                    if (
                        board[i + 1][j] == player
                        and board[i + 2][j] == player
                        and board[i + 3][j] == player
                    ):
                        return True
                if j + 3 < len(board[i]):
                    if (
                        board[i][j + 1] == player
                        and board[i][j + 2] == player
                        and board[i][j + 3] == player
                    ):
                        return True
                if i + 3 < len(board) and j + 3 < len(board[i]):
                    if (
                        board[i + 1][j + 1] == player
                        and board[i + 2][j + 2] == player
                        and board[i + 3][j + 3] == player
                    ):
                        return True
                if i - 3 >= 0 and j + 3 < len(board[i]):
                    if (
                        board[i - 1][j + 1] == player
                        and board[i - 2][j + 2] == player
                        and board[i - 3][j + 3] == player
                    ):
                        return True
    return False
