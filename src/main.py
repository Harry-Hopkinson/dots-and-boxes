import curses, sys, re
from time import sleep
from constants import *
from random import randint

stdCurses = curses.initscr()
curses.noecho()
curses.start_color()
stdCurses.keypad(1)

curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)


class Game:
    def __init__(self):
        self.self = self

    def initBoard():
        even = [False for i in range(BOARD_SIZE - 1)]
        odd = [False for i in range(BOARD_SIZE)]

        board = []
        for i in range(BOARD_SIZE * 2 - 1):
            if i % 2 == 0:
                board.append(even[:])
            else:
                board.append(even[:-1])

        return board

    def initScore():
        return [[None for a in range(BOARD_SIZE - 1)] for b in range(BOARD_SIZE - 1)]

    def closestFree(board, x, y):
        def distance(x1, y1, x2, y2):
            from math import sqrt

            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        distances = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == False:
                    distances.append((distance(x, y, i, j), i, j))

            if len(distances) == 0:
                return False

            distances.sort(key=lambda x: x[0])
            return distances[0][1:]

    def firstAvailableMove(board):
        try:
            return Game.closestFree(board, 0, 0)
        except IndexError:
            return False

    def drawDot(x, y):
        sx = OFFSET_X + x * 4
        sy = OFFSET_Y + y
        stdCurses.addstr(sy, sx, "o")
        stdCurses.addstr(sy, sx + 4, "o")

    def drawLine(x, y, colour=0):
        if y % 2 == 0:
            sy = OFFSET_Y + y
            sx = OFFSET_X + x * 4 + 1
            stdCurses.addstr(sy, sx, "---", curses.color_pair(colour))
        else:
            sy = OFFSET_Y + y
            sx = OFFSET_X + x * 4 + 1
            stdCurses.addstr(sy, sx, "|", curses.color_pair(colour))

    def drawFilling(x, y, player):
        screen_x = OFFSET_X + x * 4 + 2
        screen_y = OFFSET_Y + y * 2 + 1
        stdCurses.addstr(screen_y, screen_x, str(player), curses.color_pair(player))

    def playGame():
        board = Game.initBoard()
        score = Game.initScore()

        Game.drawBoard(board, score)

        currentPlayer = 1

        def checkSetSquare(x, y):
            if score[x][y]:
                return 0

            if (
                board[x * 2][y]
                and board[x * 2 + 1][y]
                and board[x * 2 + 1][y + 1]
                and board[x * 2 + 2][y]
            ):
                score[x][y] = current_player
                return 1

        return 0

        selectedX, selectedY = 0, 0

        while Game.firstAvailableMove(board):
            y = OFFSET_Y + BOARD_SIZE * 2 + 1

            selectedX, selectedY = Game.closestFree(board, selectedX, selectedY)

            c = None
            while c != ord("\n") or board[selectedX][selectedY]:
                stdCurses.clear()
                Game.drawBoard(board, score)
                colour = board[selectedX][selectedY] and 3 or currentPlayer
                Game.drawLine(selectedX, selectedY, colour)

                c = stdCurses.getch()
                if c == curses.KEY_UP:
                    size = selectedX % 2 == 0 and 2 * BOARD_SIZE - 1 or 2 * BOARD_SIZE
                    selectedX = (selectedX - 1) % size

                    if selectedY >= len(board[selectedX]):
                        selectedY = len(board[selectedX]) - 1
                    elif selectedY == len(board[selectedX]) - 2 and selectedX % 2 == 1:
                        selectedY += 1
                elif c == curses.KEY_DOWN:
                    size = selectedX % 2 == 0 and 2 * BOARD_SIZE - 1 or 2 * BOARD_SIZE
                    selectedX = (selectedX + 1) % size

                    if selectedY >= len(board[selectedX]):
                        selectedY = len(board[selectedX])
                    elif selectedY == len(board[selectedX] - 2 and selectedX % 2 == 1):
                        selectedY += 1
                elif c == curses.KEY_LEFT:
                    size = selectedX % 2 == 0 and BOARD_SIZE - 1 or BOARD_SIZE
                    selectedY = (selectedY - 1) % size
                elif c == curses.KEY_RIGHT:
                    size = selectedX % 2 == 0 and BOARD_SIZE - 1 or BOARD_SIZE
                    selectedY = (selectedY + 1) % size

            x1, y1 = selectedX, selectedY

            filledBoxes = 0
            board[selectedX][selectedY] = True

            if selectedX % 2 == 0:
                if x1 > 0:
                    filledBoxes += checkSetSquare((x1 - 1) / 2, y1)

                if (x1 - 1) / 2 + 1 < BOARD_SIZE - 1:
                    filledBoxes += checkSetSquare((x1 - 1) / 2 + 1, y1)
            else:
                if y1 > 0:
                    filledBoxes += checkSetSquare((x1 - 1) / 2, y1 - 1)

                if y1 < BOARD_SIZE - 1:
                    filledBoxes += checkSetSquare((x1 - 1) / 2, y1)

                if filledBoxes == 0:
                    current_player = current_player % 2 + 1

                Game.drawBoard()
                stdCurses.refresh()

        def drawBoard(board, score):
            for i, row in enumerate(board):
                print("https://gist.github.com/stephenroller/3163995")


if __name__ == "__main__":
    try:
        Game.playGame()
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()
