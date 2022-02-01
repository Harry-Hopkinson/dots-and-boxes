from constants import *
import pygame
from pygame.locals import *
from tryStatement import *
pygame.init()
https: // stackoverflow.com/questions/46843897/how-to-draw-a-circle-in-pygame/46843934

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def getPos():
    pos = pygame.mouse.get_pos()
    return pos


def drawCircle():
    pos = getPos()
    pygame.draw.circle(screen, BLACK, pos, 20)
