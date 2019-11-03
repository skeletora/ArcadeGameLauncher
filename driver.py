from gameClass import GameClass, GameListClass
from infoMenu import InfoMenu
from controlsMenu import ControlsMenu
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


def CheckPress(event, moveCount, menu, info = False, controls = False):

    pos = None
    pos2 = None
    pos3 = None

    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN and info == False and controls == False:
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
        if not info and not controls: 
            pos = menu.CheckClick(pygame.mouse)
        elif info and not controls: 
            pos2 = infoMenu.CheckClick(pygame.mouse)
        elif controls and not info: 
            pos3 = controlsMenu.CheckClick(pygame.mouse)

    return moveCount, pos, pos2, pos3

def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

pygame.init()

menu = Menu(pygame.display.set_mode((1366, 768), pygame.NOFRAME), GameListClass())
infoMenu = None
controlsMenu = None
toplist = []
winlist = []

moveCount = 0
pos = None
pos2 = None
pos3 = None
infoActive = False
controlsActive = False
MAX_SPEED = 12


menu.Draw()
while True:

    for event in pygame.event.get():
        moveCount, pos, pos2, pos3 = CheckPress(event, moveCount, menu, infoActive, controlsActive)

    if pos is not None:
        infoMenu = InfoMenu(pygame.display.set_mode((1366, 768), pygame.NOFRAME), menu.buttons[pos].game)
        infoMenu.Draw()
        moveCount = 0
        pos = None
        infoActive = True

    if pos2 is not None:
        if pos2 == 0:
            menu.screen.fill((0, 0, 0))
            pygame.display.flip()
            game = subprocess.Popen('"' + infoMenu.buttons[pos2].game.game + '"')
            #Code to minimize launcher
            win32gui.EnumWindows(enum_callback, toplist)
            pygameW = [(hwnd, title) for hwnd, title in winlist if 'pygame' in title.lower()]
            pygameW = pygameW[0]
            win32gui.SetForegroundWindow(pygameW[0])
            win32gui.ShowWindow(pygameW[0], win32con.SW_HIDE)
		    # Everything that needs to happen at game launch needs to be before this.
            game.wait()
		    # Once game terminates, redraw and maximize.
            menu.Draw()
            pos2 = None
            infoActive = False
            win32gui.ShowWindow(pygameW[0], win32con.SW_SHOW)
        elif pos2 == 1:
            controlsMenu = ControlsMenu(pygame.display.set_mode((1366,768), pygame.NOFRAME), infoMenu.buttons[0].game)
            controlsMenu.Draw()
            pos2 = None
            infoActive = False
            controlsActive = True
        elif pos2 == 2:
            pos2 = None
            infoActive = False
            menu.Draw()
			
    if pos3 is not None:
        if pos3 == 0:
            menu.screen.fill((0, 0, 0))
            pygame.display.flip()
            game = subprocess.Popen('"' + infoMenu.buttons[pos3].game.game + '"')
            #Code to minimize launcher
            win32gui.EnumWindows(enum_callback, toplist)
            pygameW = [(hwnd, title) for hwnd, title in winlist if 'pygame' in title.lower()]
            pygameW = pygameW[0]
            win32gui.SetForegroundWindow(pygameW[0])
            win32gui.ShowWindow(pygameW[0], win32con.SW_HIDE)
		    # Everything that needs to happen at game launch needs to be before this.
            game.wait()
		    # Once game terminates, redraw and maximize.
            menu.Draw()
            pos3 = None
            controlsActive = False
            win32gui.ShowWindow(pygameW[0], win32con.SW_SHOW)
        elif pos3 == 1:
            pos3 = None
            controlsActive = False
            infoActive = True
            infoMenu.Draw()

    if moveCount != 0:
        menu.Rotate(moveCount)
        menu.Draw()

