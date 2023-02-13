"""
file        : tictactoe.py
author      : Dulli25
description : simple tic-tac-toe game
libs        : pygame
"""
import pygame
from pygame.locals import *
pygame.font.init()
my_font = pygame.font.SysFont('Verdana', 30)

#colors
RED = (255,0,0)
GRAY = (127,127,127)
LIGHTGRAY = (220,220,220)
WHITE = (255,255,255)
BLUE = (30,144,255)
BLACK = (0,0,0)

#define general colors
color_background = LIGHTGRAY
color_grid = BLACK

#defining important vars
screen = pygame.display.set_mode((300,500))
pygame.display.set_caption("Python Tic-Tac-Toe")
screen.fill(color_background)
def arr_empty(): return [0,0,0,0,0,0,0,0,0]
arr_game = arr_empty()
running = True
placeable = True

#inportant variables for the game to work
turn = "O"  #defines which player's turn it is; either O or X
counter_O = 0   #counts points of player O
counter_X = 0   #counts points of player X
status = "Start"    #content of the text box below the field

#images
image_x = pygame.image.load("TicTacToe/X.png")
image_o = pygame.image.load("TicTacToe/O.png")
image_x = pygame.transform.scale(image_x, (90,90))
image_o = pygame.transform.scale(image_o, (90,90))

#images next to counter
screen.blit(pygame.transform.scale(image_x, (50,50)), (25,360))
screen.blit(pygame.transform.scale(image_o, (50,50)), (225,360))

#rendering text
text_counter = my_font.render(str(counter_X) + " : " + str(counter_O), False, BLACK)
text_counter_pos = (115,360)
text_status = my_font.render(status, False, BLACK)
text_status_pos = (50, 310)

#buttons
#button reset
button_reset_rect = pygame.Rect(100,430, 100, 50)
pygame.draw.rect(screen, GRAY, button_reset_rect, 3)
button_reset_text = my_font.render("Reset", False, BLACK)
button_reset_textpos = (111, 431)
screen.blit(button_reset_text, button_reset_textpos)


#functions ------------------------------------------------------------------------------------------------------------------

def drawGrid(): #drawing the grid once
    blocksize = 100
    for x in range(0,300,blocksize):
        for y in range(2,300,blocksize):
            rect = pygame.Rect(x,y, blocksize, blocksize)
            pygame.draw.rect(screen, color_grid, rect, 3)

def drawGame(): #drawing the gameboard
    global arr_game
    blocksize = 10
    indx = 0
    for y in range(0,300,100):
        for x in range(0,300,100):
            if arr_game[indx] == 1:
                screen.blit(image_o,(x+5,y+5))
            if arr_game[indx] == 2:
                screen.blit(image_x, (x+5,y+5))
            indx += 1

def findBlock(x,y): #find block in which the mouse is
    if(x < 100):
        if(y < 100):
            return 0
        if(y > 100 and y < 200):
            return 3
        if(y > 200 and y < 300):
            return 6
    if(x > 100 and x < 200):
        if(y < 100):
            return 1
        if(y > 100 and y < 200):
            return 4
        if(y > 200 and y < 300):
            return 7
    if(x > 200):
        if(y < 100):
            return 2
        if(y > 100 and y < 200):
            return 5
        if(y > 200 and y < 300):
            return 8
        
def playerInput(x,y): #on input change 
    global turn,arr_game, status
    block = findBlock(x,y)
    if arr_game[block] == 0:
        if turn == "O":
            arr_game[block] = 1
            turn = "X"
            status = "X turn"
        elif turn == "X":
            arr_game[block] = 2
            turn = "O"
            status = "O turn"
    
def game_reset(): #reset game arr back to emptay array
    global arr_game, status, placeable
    arr_game = arr_empty()
    status = "Start"
    placeable = True

def counter_add(player): #adding points to the counter
    global counter_O,counter_X, text_counter
    if player == "O":
        counter_O += 1
    if player == "X":
        counter_X += 1
    text_counter = my_font.render(str(counter_X) + " : " + str(counter_O), False, (BLACK))

def render_all(): #function that renders all things on the display
    screen.fill(color_background)
    drawGrid()
    drawGame()
    screen.blit(text_counter,text_counter_pos)
    screen.blit(pygame.transform.scale(image_x, (50,50)), (25,360))
    screen.blit(pygame.transform.scale(image_o, (50,50)), (225,360))
    pygame.draw.rect(screen, GRAY, button_reset_rect, 3)
    screen.blit(button_reset_text, button_reset_textpos)
    text_status = my_font.render(status, False, BLACK)
    screen.blit(text_status, text_status_pos)

def findWin(): #function that searches for a win on the field by comparing to possible wins
    global arr_game, status, placeable
    arr_x = arr_empty()
    arr_o = arr_empty()
    cx = 0
    co = 0
    c = 0
    indx = 0
    wins = [[1,1,1,0,0,0,0,0,0], 
            [0,0,0,1,1,1,0,0,0], 
            [0,0,0,0,0,0,1,1,1], 
            [1,0,0,1,0,0,1,0,0], 
            [0,1,0,0,1,0,0,1,0],
            [0,0,1,0,0,1,0,0,1],
            [1,0,0,0,1,0,0,0,1],
            [0,0,1,0,1,0,1,0,0]]
    for x in arr_game:
        if x == 1:
           arr_o[indx] = 1             
        if x == 2:
            arr_x[indx] = 1
        indx += 1
    c = 0
    for x in wins:
        cx = 0
        co = 0
        for y in x:
            if arr_x[c] == y and arr_x[c] != 0:
                cx += 1
            if arr_o[c] == y and arr_o[c] != 0:
                co += 1
            c += 1
        c = 0
        if co == 3:
            status = "O WINS"
            placeable = False
            counter_add("O")
            return
        if cx == 3:
            status = "X WINS"
            placeable = False
            counter_add("X")
            return

def log(log):   #logs to the console for maintaince 
    print("LOG: " + log)

#main --------------------------------------------------------------------------------------------------------------------------------------------
drawGrid()
drawGame()
while running: #main game loop
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_0:
                counter_add("O")
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if(y < 300 and placeable):
                playerInput(x,y)
            if(x > 100 and x < 200 and y > 430 and y < 480):
                game_reset()
            drawGame()
        if placeable: findWin()
    render_all()
    pygame.display.update()
    
pygame.quit()

