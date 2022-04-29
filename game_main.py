from operator import invert
from re import S
from matplotlib.pyplot import text
import numpy as np
import pygame as p
import game_engine

p.init()

WIDTH = HEIGHT = 512
dims = 4
SQ_size = HEIGHT // dims
max_fps = 15
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

pieces = {}
for i, num in enumerate(nums):
    if i % 2 == 0:
        color = p.Color('white')
    else:
        color = p.Color('maroon')
    s = p.Surface((SQ_size * 0.99, SQ_size * 0.99))
    s.fill(color)
    pieces[num] = p.Surface((SQ_size * 0.99, SQ_size * 0.99))

print(pieces)


def main():
    #Loading screen flag (currently false until loading screen is built)
    loading_screen = False
    pattern = 1

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    p.display.set_caption("Chase's Fun Fifteen Game")
    draw_squares(screen)

    if not loading_screen:
        play_game(screen, pattern, clock)

def play_game(screen, pattern, clock):
    screen.fill(p.Color("white"))
    gs_final = game_engine.gameBoard(pattern)
    gs_current = game_engine.gameBoard(pattern)
    gs_current.shuffle()
    current_moves = gs_current.valid_moves()
    running = True
    #Stores where the player has clicked and if a square is selected/which one
    selected_square = ()
    player_clicks = []
    #Used to determine if game has been won
    game_done = False
    #Stores if a move has just been been made
    move_made = False

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                if not game_done:
                    col = location[0] // SQ_size
                    row = location[1] // SQ_size
                    #Checks to see if move is to a different square
                    if selected_square == (row, col):
                        selected_square = ()
                        player_clicks = []
                    else:
                        selected_square = (row, col)
                        player_clicks.append(selected_square)
                    #Checking if click is second click inicating a piece move
                    if len(player_clicks) == 2:
                        move = game_engine.move(player_clicks[1], player_clicks[0], gs_current.board)
                        #checking if valid
                        if move in current_moves:
                            gs_current.make_move(move)
                            selected_square = ()
                            player_clicks = []
                            move_made = True
                        #minimizing clicks
                        if not move_made:
                            player_clicks = [selected_square]

            if move_made:
                if np.array_equal(gs_current.board, gs_final.board):
                    game_done = True
                current_moves = gs_current.valid_moves()
                move_made = False

            if game_done:
                draw_text(screen, "Congrats! You won!", 0)

            draw_game_board(screen, gs_current, current_moves, selected_square)
            clock.tick(max_fps)
            p.display.flip()
                
def draw_game_board(screen, gs, valid_moves, selected_sq):
    draw_squares(screen) #draws squares on board
    draw_pieces(screen, gs.board) #draws pieces on top of squares

#Draws squares on the board
def draw_squares(screen):
    global colors
    colors = [p.Color("green"), p.Color("yellow")]
    for row in range(dims):
        for col in range(dims):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_size, row*SQ_size, SQ_size, SQ_size))

def draw_pieces(screen, board):
    for row in range(dims):
        for col in range(dims):
            piece = board[row, col]
            if piece != "--":
                x = pieces[piece]
                p.draw.rect(screen, p.Color('brown'), p.Rect(col*SQ_size, row*SQ_size, SQ_size, SQ_size))

def draw_text(screen, text, opacity):
    font = p.font.SysFont("Helvitca", 45, True, False)
    text_object = font.render(text, opacity, p.Color("Red"))
    text_location = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2, HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, opacity, p.Color("Blue"))
    screen.blit(text_object, text_location.move(2, 2))

if __name__ == "__main__":
    main()




