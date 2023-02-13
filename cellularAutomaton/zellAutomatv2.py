import pygame
from pygame.locals import *
import random
from random import randrange
import os
import time


displaysize = (1200,1000)

#colors
WHITE = (255,255,255)
GREY = (100,100,100)
BLACK = (0,0,0)

arr_game = list()
arr_coord = list()
run = True
counter = 0
start = False

screen = pygame.display.set_mode(displaysize)
pygame.display.set_caption("Evolution v2")
screen.fill(WHITE)
pygame.display.update()

#functions - - -- - -- -- -- - - -- - -- -- -- - --- -
def drawRect(posx,posy,state):
    rect = pygame.Rect(posx,posy,10,10)
    if state == 1:
        pygame.draw.rect(screen,BLACK,rect,10)
    if state == 0:
        pygame.draw.rect(screen,WHITE,rect,10)

def init():
    global arr_coord,arr_game
    print("Loading. . . ")
    for y in range(0,100,1):
        for x in range(0,100,1):
            arr_coord.append((x,y))
    arr_game = [0] * 10000
    print("Init complete!")

def findState(x,y):
    global arr_coord, arr_game
    try: 
        indx = arr_coord.index((x,y))
        return arr_game[indx]
    except:
        return 0

def findIndex(x,y):
    global arr_coord
    return arr_coord.index((x,y))

def drawField():
    global arr_coord, arr_game
    for y in range(0,1000,10):
        for x in range(0,1000,10):
            drawRect(x,y,findState(x/10,y/10))

def drawGrid():
    for y in range(0,1000,10):
        for x in range(0,1000,10):
            rect = pygame.Rect(x,y,10,10)
            pygame.draw.rect(screen, GREY, rect, 1)


def drawInterface():
    rect = pygame.Rect(0,0,1000,1000)
    pygame.draw.rect(screen,BLACK,rect,1)
    rect = pygame.Rect(1000,0,200,1000)
    pygame.draw.rect(screen,BLACK,rect,1)
    pygame.display.update()

def countAround(x,y):
    counter = 0
    counter = findState(x+1,y) + findState(x-1,y) + findState(x,y+1) + findState(x,y-1)
    counter += findState(x+1,y+1) + findState(x+1,y-1) + findState(x-1,y-1) + findState(x-1,y+1)
    return counter

def updateCell(x,y):
    global arr_game
    arr_puff = arr_game
    indx = findIndex(x,y)
    count = countAround(x,y)
    if count == 3:
        arr_puff[indx] = 1
    if count < 2:
        arr_puff[indx] = 0
    if arr_game[indx] == 1 and count >= 2 and count <= 3:
        arr_puff[indx] = 1
    if count > 3:
        arr_puff[indx] = 0
    arr_game = arr_puff

def drawAll():
    screen.fill(WHITE)
    drawField()
    drawGrid()
    drawInterface()
    pygame.display.update()

def coordsForMouse(mx,my):
    pass



# - - - -- - -- - -- - - -- -- - - - --            -- - -- - -- - -- - -- 

init()
drawAll()
while run:

    start_time = time.time()

    if start:
        #time.sleep(1)
        drawAll()
        counter += 1
        print(counter)
        for i in arr_coord:
            x,y = i
            updateCell(x,y)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            if start == False:
                start = True
                print("Game Start!")
            else:
                start = False
                print("Game Stop!")
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    pygame.display.update()
    print("--- %s seconds ---" % (time.time() - start_time))


pygame.quit()