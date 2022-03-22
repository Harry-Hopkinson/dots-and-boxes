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


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


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
    
while True:
    endGame(board)
    printBoard(board)
    print("Player 1:")
    i = int(input("Row: "))
    j = int(input("Column: "))
    endGame(board)
    if play(board, 1, i, j):
        print("Player 2:")
        i = int(input("Row: "))
        j = int(input("Column: "))
        if play(board, -1, i, j):
            pass
    else:
        print("Invalid move")

