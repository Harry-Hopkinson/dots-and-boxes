from tkinter import *
from archive.constants import *


class DotsAndBoxes:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dots_and_Boxes")
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        self.window.bind("<Button-1>", self.click)
        self.player1_starts = True
        self.refresh_board()
        self.play_again()

    def play_again(self):
        self.refresh_board()

        self.player1_starts = not self.player1_starts
        self.player1_turn = not self.player1_starts
        self.reset_board = False
        self.turntext_handle = []

        self.already_marked_boxes = []
        self.display_turn_text()
        return self

    def refresh_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.display_turn_text()
        return self

    def click(self):
        return print("Hello World")

    def draw_board(self):
        print("Drawing Board")

    def display_turn_text(self):
        return print("Displaying Text")

    def turn_text(self):
        return print("Turning Text")

    def mainloop(self):
        return self.canvas.mainloop()


gameInsance = DotsAndBoxes()
gameInsance.mainloop()
