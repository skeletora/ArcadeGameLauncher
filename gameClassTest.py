from gameClass import GameClass, GameListClass
import os, sys
import pygame
pygame.init()

def Exit():
	response = input("Test? (y or n) ")
	
	if response == 'y':
		return False
	else:
		return True

games = GameListClass()	
		
while not Exit():
	print("\nTesting\n............................\n")
	
	for game in games.gamesList:
		print("The game is: %s" %(game.game))
		score = input("Rate this game (0-10): ")
		game.AddRating(score)
		
		print("\n\nThe game's new score is: %s / 10" %game.Rating())
		
			