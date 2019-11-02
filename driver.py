from GameButton import GameButton
from menu import Menu
import sys, pygame

def InitImages():
    images = ["DemoPics/Game1/thumb.jpg", "DemoPics/Game2/thumb.jpg", "DemoPics/Game3/thumb.jpg",
              "DemoPics/Game4/thumb.jpg", "DemoPics/Game5/thumb.jpg", "DemoPics/Game6/thumb.jpg",
              "DemoPics/Game7/thumb.jpg", "DemoPics/Game8/thumb.jpg"]
    return images


def CheckPress(event, moveCount):


    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_LEFT:
            moveCount = moveCount + 3
        elif event.key == pygame.K_RIGHT:
            moveCount = moveCount - 3

    if moveCount > MAX_SPEED:
        moveCount = MAX_SPEED
    elif moveCount < -MAX_SPEED:
        moveCount = -MAX_SPEED

    return moveCount


pygame.init()
menu = Menu(pygame.display.set_mode((0, 0), pygame.FULLSCREEN), InitImages())
moveCount = 0
MAX_SPEED = 12

menu.Draw()
while True:
    for event in pygame.event.get():
        moveCount = CheckPress(event, moveCount)

    if moveCount != 0:
        menu.Rotate(moveCount)
        menu.Draw()