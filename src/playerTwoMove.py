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