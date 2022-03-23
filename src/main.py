from constants import *

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


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def resetBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0


def play(board, player, i, j):
    if i < 0 or i > 4 or j < 0 or j > 4:
        return False
    if board[i][j] == 0:
        board[i][j] = player
        if player == 1:
            player = -1
        else:
            player = 1
        return player
    else:
        return False


def endGame(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True


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


def checkDraw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True


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


def playerTwoMove(board):
    while True:
        i = int(input("Enter row: "))
        j = int(input("Enter column: "))
        if play(board, -1, i, j):
            break
        else:
            print("Invalid move")
    printBoard(board)
    if checkWin(board, -1):
        print("Player 2 wins")
        printBoard(board)
        return True
    elif checkDraw(board):
        print("Draw")
        return True
    else:
        return False

running = True

while running:
    printBoard(board)
    if playerOneMove(board):
        running = False
    if playerTwoMove(board):
        running = False

playAgain = input("Play again? (y/n): ")
if playAgain == "y":
    resetBoard(board)
    running = True

print("Thanks for playing!")
