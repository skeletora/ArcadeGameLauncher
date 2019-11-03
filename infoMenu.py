from gameClass import GameClass, GameListClass
from GameButton import GameButton
from MenuButton import MenuButton
import collections as col
import sys, pygame

LAUNCHERPATH="C:\Launcher"
BUTTONSIZE=128

class InfoMenu:

	def __init__(self, screen, game):
		self.screen = screen
		self.width, self.height = pygame.display.get_surface().get_size()
		self.background = LAUNCHERPATH + '\darkenedbackground.png'
		self.menu = pygame.transform.scale(pygame.image.load(self.background).convert_alpha(), (self.width, self.width))

		self.game = game
		
		with open(self.game.info) as f:
			self.info = f.read()

		self.buttons = self.InitButtons()
		self.titleFont = pygame.font.SysFont('oldenglishtext', 64)
		self.font = pygame.font.SysFont('Arial', 32)
		self.cursor = 0

	def InitButtons(self):
		buttons = col.deque()
		newButton = GameClass()
		#Create "play game" button
		newButton.SetGame(self.game.game)
		newButton.SetControls(self.game.controls)
		newButton.SetImage(LAUNCHERPATH + '\playbutton.png')
		
		buttons.append(MenuButton(newButton, BUTTONSIZE, BUTTONSIZE))
		buttons[-1].Move(self.width-BUTTONSIZE-20,100)
		
		#Create "controls" button
		newButton.SetImage(LAUNCHERPATH + '\controlsbutton.png')
		buttons.append(MenuButton(newButton, BUTTONSIZE, BUTTONSIZE))
		buttons[-1].Move(self.width-BUTTONSIZE*2-40,100)
		
		#Create "go back" button
		newButton.SetImage(LAUNCHERPATH + '\cbackbutton.png')
		buttons.append(MenuButton(newButton, BUTTONSIZE, BUTTONSIZE))
		buttons[-1].Move(self.width-BUTTONSIZE*3-60,100)

		return buttons
		
	def MakeText(self, surface, text, pos, font, color=pygame.Color('white')):
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
		self.screen.blit(self.menu, (0,0))
		
		for i in self.buttons:
			self.screen.blit(i.img, i.pos)
			
		self.MakeText(self.screen, self.info, (100, self.height*(1/3)), self.font)
		self.MakeText(self.screen, "Game Info!", (100, 100), self.titleFont)
		
		pygame.display.flip()

	def CheckClick(self, mouse):
		pos = mouse.get_pos()
		clicked = None
		
		for i,b in enumerate(self.buttons):
			if b.CheckClicked(pos):
				clicked = i
		
		return clicked