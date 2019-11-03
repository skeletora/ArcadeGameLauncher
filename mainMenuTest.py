from mainMenu import MainMenu
import pygame
import sys
import time

pygame.init()

def Exit():
	response = input("Test? (y or n) ")
	
	if response == "y":
		return False
	else:
		return True

menu = MainMenu(pygame.display.set_mode((0, 0), pygame.FULLSCREEN), 
		pygame.font.Font("C:/Windows/Fonts/OLDENGL.ttf", 50))


menu.Draw()

while True:
	menu.Move()

	'''
	time.sleep(5)
	break
	'''