from gameClass import GameClass, GameListClass
from infoMenu import InfoMenu
from menu import Menu
import sys
import pygame
import subprocess
import os
import win32gui
import win32con
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

def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

pygame.init()

menu = Menu(pygame.display.set_mode((1366, 768), pygame.NOFRAME), GameListClass())
toplist = []
winlist = []

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
		# Code to minimize launcher
        win32gui.EnumWindows(enum_callback, toplist)
        pygameW = [(hwnd, title) for hwnd, title in winlist if 'pygame' in title.lower()]
        pygameW = pygameW[0]
        win32gui.SetForegroundWindow(pygameW[0])
        win32gui.ShowWindow(pygameW[0], win32con.SW_HIDE)
		# Everything that needs to happen at game launch needs to be before this.
        game.wait()
		# Once game terminates, redraw and maximize.
        menu.Draw()
        moveCount = 0
        pos = None
        win32gui.ShowWindow(pygameW[0], win32con.SW_SHOW)

    if moveCount != 0:
        menu.Rotate(moveCount)
        menu.Draw()

