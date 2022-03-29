from constants import *

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


class Game():
    def __init__(self):
        self.gameOver = False

    def printBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    print(".", end="")
                elif board[i][j] == 1:
                    print("x", end="")
                elif board[i][j] == -1:
                    print("o", end="")
            print()
        if game.gameOver:
            print("Game Over")
            return False
       

    def resetBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = 0

    def play(self, board, player, i, j):
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

    def endgame(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    return False
        return True

    def checkWin(self, board, player):
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

    def checkDraw(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    return False
        return True

    def playerOneMove(self, board):
        while True:
            i = int(input("Enter row: "))
            j = int(input("Enter column: "))
            if game.play(board, 1, i, j):
                break
            else:
                print("Invalid move")
        game.printBoard(board)
        if game.checkWin(board, 1):
            print("Player 1 wins")
            game.printBoard(board)
            return True
        elif game.checkDraw(board):
            print("Draw")
            return True
        else:
            return False

    def playerTwoMove(self, board):
        while True:
            i = int(input("Enter row: "))
            j = int(input("Enter column: "))
            if game.play(board, -1, i, j):
                break
            else:
                print("Invalid move")
        if game.checkWin(board, -1):
            print("Player 2 wins")
            game.printBoard(board)
            return True
        elif game.checkDraw(board):
            print("Draw")
            return True
        else:
            return False


running = True
game = Game()

def main():
    while running:
        game.printBoard(board)
        while not game.endgame(board):
            if game.playerOneMove(board):
                break
            if game.playerTwoMove(board):
                break
        running = False

playAgain = input("Play again? (y/n): ")
if playAgain == "y":
    game.resetBoard(board)
    main()

print("Thanks for playing!")
