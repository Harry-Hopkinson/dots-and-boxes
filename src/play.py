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
