from gameClass import GameClass, GameListClass
from GameButton import GameButton
import collections as col
import sys, pygame

LAUNCHERPATH="C:\Launcher"

class InfoMenu:

	def __init__(self, screen, game):
		self.screen = screen
		self.ON_SCREEN = 5
		self.width, self.height = pygame.display.get_surface().get_size()

		self.game = game
		
		with open(self.game.info) as f:
			self.info = f.read()

		self.buttons = self.InitButtons()
		self.font = font = pygame.font.SysFont('Arial', 32)
		self.cursor = 0

	def InitButtons(self):
		buttons = col.deque()
		newButton = GameClass()
		newButton.SetImage(LAUNCHERPATH + '\playbutton.png')
		
		buttons.append(GameButton(newButton))

		return buttons
		
	def MakeText(self, surface, text, pos, font, color=pygame.Color('black')):
		tokens = [word.split(' ') for word in text.splitlines()]
		space = font.size(' ')[0]
		max_width, max_height = surface.get_size()
		x, y = pos
		for line in tokens:
			for word in line:
				token_surface = font.render(word, 0, color)
				token_width, token_height = token_surface.get_size()
				if x + token_width >= max_width:
					x = pos[0]
					y += token_height
				surface.blit(token_surface, (x, y))
				x += token_width + space
			x = pos[0]
			y += token_height

	def Draw(self):
		self.screen.fill((255,255,255))
		
		for i in self.buttons:
			self.screen.blit(i.img, i.pos)
			
		self.MakeText(self.screen, self.info, (20, 20), self.font)
		
		pygame.display.flip()

	def CheckClick(self, mouse):
		pos = mouse.get_pos()
		clicked = None
		
		for i,b in enumerate(self.buttons):
			if b.CheckClicked(pos):
				clicked = i
		
		return clicked