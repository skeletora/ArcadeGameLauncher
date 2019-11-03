from gameClass import GameClass, GameListClass
from GameButton import GameButton
import collections as col
import sys, pygame

class InfoMenu:

    def __init__(self, screen, games):
		self.screen = screen
		self.ON_SCREEN = 5
		self.width, self.height = pygame.display.get_surface().get_size()

		self.gameList = games

		self.bNames = []
		for game in self.gameList.gamesList:
			self.bNames.append(game.image)

		self.buttons = self.InitButtons(self.bNames)
		self.cursor = 0

	def InitButtons(self, names):
		buttons = col.deque()
		for i in range(self.ON_SCREEN):
			buttons.append(GameButton(self.gameList.gamesList[i]))
			buttons[-1].Move(612*(i-.5), self.height/4)

		return buttons

	def Draw(self):
		self.screen.fill((255,255,255))
		
		for i in self.buttons:
			self.screen.blit(i.img, i.pos)
		pygame.display.flip()

	def CheckClick(self, mouse):
		pos = mouse.get_pos()
		clicked = None
		
		for i,b in enumerate(self.buttons):
			if b.CheckClicked(pos):
				clicked = i
		
		return clicked