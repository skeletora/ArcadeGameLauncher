from gameClass import GameClass, GameListClass
from menu import Menu
import sys
import pygame
import subprocess
import os
from time import sleep
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 0'

def InitImages():
    images = ["DemoPics/Game1/thumb.jpg", "DemoPics/Game2/thumb.jpg", "DemoPics/Game3/thumb.jpg",
              "DemoPics/Game4/thumb.jpg", "DemoPics/Game5/thumb.jpg", "DemoPics/Game6/thumb.jpg",
              "DemoPics/Game7/thumb.jpg", "DemoPics/Game8/thumb.jpg"]
    return images


def CheckPress(event, moveCount, menu):

    pos = None

    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            moveCount = moveCount + 3
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            moveCount = moveCount - 3
        if moveCount > MAX_SPEED:
            moveCount = MAX_SPEED
        elif moveCount < -MAX_SPEED:
            moveCount = -MAX_SPEED
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = menu.CheckClick(pygame.mouse)

    return moveCount, pos



pygame.init()

menu = Menu(pygame.display.set_mode((1920, 1080), pygame.NOFRAME), GameListClass())


moveCount = 0
pos = None
MAX_SPEED = 12


menu.Draw()
while True:

    for event in pygame.event.get():
        moveCount, pos = CheckPress(event, moveCount, menu)

    if pos is not None:
        menu.screen.fill((0, 0, 0))
        pygame.display.flip()
        game = subprocess.Popen('"' + menu.buttons[pos].game.game + '"')
        game.wait()
        menu.Draw()
        moveCount = 0
        pos = None

    if moveCount != 0:
        menu.Rotate(moveCount)
        menu.Draw()

