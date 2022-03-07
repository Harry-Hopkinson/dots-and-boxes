import tkinter

root = tkinter.Tk()
from constants import *

### Dots and Boxes in the Terminal ###

## Screen ##
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (width, height))
root.focus_set()
root.bind("<Escape>", lambda e: (e.widget.withdraw(), root.destroy()))
root.configure(background="white")
canvas = tkinter.Canvas(root, width=width, height=height, background="white")
canvas.pack()


def draw_circle(x, y, r, colour):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=colour)
    return None


for i in range(7):
    for n in range(7):
        draw_circle(width / 7 * i, height / 7 * n, 5, "black")


### Tkinter Roots ###
canvas.pack()
root.mainloop()
