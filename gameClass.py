import os, sys
import pygame
pygame.init()

STARTPATH = "C:\Games"
NOT_THERE = "NA"

class GameClass:
	"This stores all of the game's data"
	def __init__(self):
		self.game = NOT_THERE
		self.image = NOT_THERE
		self.info = NOT_THERE
		self.controls = NOT_THERE
		self.music = NOT_THERE
		self.ratings = []
	
	def SetGame(self, filePath):
		self.game = filePath
	
	def SetImage(self, imagePath):
		self.image = imagePath
		
	def SetInfo(self, infoPath):
		self.info = infoPath
		
	def SetControls(self, ctrlPath):
		self.controls = ctrlPath
	
	def SetMusic(self, musicPath):
		self.music = musicPath
		
	def AddRating(self, score):
		if int(score) > 10:
			score = 10
		if int(score) < 0:
			score = 0
		self.ratings.append(int(score))
		
	def Rating(self):
		rating = 0
		
		for score in self.ratings:
			rating = rating + score
			
		rating = rating / len(self.ratings)
		
		return round(rating, 2)

class GameListClass:
	"Generates and stores a list of all the games in the system"
	
	def __init__(self):
		self.gamesList = self.GenerateGameList()
		
		
	def GenerateGameList(self):
		folders = os.listdir(STARTPATH)
		list = []
		game = GameClass()
		add = False
		
		for folder in folders:
			temp = os.path.join(STARTPATH, folder)
			temp2 = os.listdir(temp)
			
			for file in temp2:
				path = os.path.join(temp, file)
				path = '"%s"' %(path)
				
				if file.endswith(".exe"):
					game.SetGame(path)
					add = True
				if file.endswith(".jpg"):
					game.SetImage(path)
					add = True
				if file == "Info.txt":
					game.SetInfo(path)
					add = True
				if file == "Controls.txt":
					game.SetControls(path)
					add = True
				if file.endswith(".mp3"):
					game.SetMusic(path)
					add = True
			if add:
				list.append(game)
				game = GameClass()
				add = False
					
		return list

	def UpdateList(self):
		gamesList = self.GenerateGameList()