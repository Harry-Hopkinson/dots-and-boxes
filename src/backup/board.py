def boardShape(boardString):
    lines = boardString.split("|")
    rows, cols = (len(lines) + 1) / 2, (len(lines[0]) + 1) / 2
    return rows, cols