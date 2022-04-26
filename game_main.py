from operator import invert
from re import S
from matplotlib.pyplot import text
from numpy import squeeze
import pygame as p

p.init()

WIDTH = HEIGHT = 512
dims = 4
SQ_size = HEIGHT // dims
max_fps = 15

pieces = {}
for i in range(1, 16):
    pieces[str(i)]

def main():
    #Loading screen flag
    loading_screen = True
    pattern = 1

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()

    if not loading_screen:
        play_game(screen, pattern)

def play_game(screen, pattern):
    return False

#Draws squares on the board
def draw_squares(screen):
    global colors
    colors = [p.Color("white"), p.Color("maroon")]
    for row in range(dims):
        for col in range(dims):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_size, row*SQ_size, SQ_size, SQ_size))