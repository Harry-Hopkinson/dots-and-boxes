import curses, sys, re
from time import sleep
from constants import *
from random import randint

stdCurses = curses.initscr()
curses.noecho()
curses.start_color()
stdCurses.keypad(1)