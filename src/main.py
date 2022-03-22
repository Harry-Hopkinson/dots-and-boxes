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
printBoard(board)
