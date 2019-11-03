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


#menu.Draw()

start = 0
end = 10

while start < end:
	#menu.Move()
	print(start)
	print("\n\n\n\n")
	start = menu.Learp(start, end, start)
	print(start)
	print("\n\n\n\n")

	'''
	time.sleep(5)
	break
	'''