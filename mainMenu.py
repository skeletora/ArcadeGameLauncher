import sys
import pygame
from random import randrange
import time
pygame.init()

'''
class FontClass:
	def __init__(self, font, x, y):
'''
		

class MainMenu:
	def __init__(self, screen, font):
		self.background = "C:/Users/r813486a/Documents/ArcadeGameLauncher/MenuGraphics/arcadetitle.png"
		self.screen = screen
		self.width, self.height = pygame.display.get_surface().get_size()
		
		self.font = font
		self.text = self.font.render("Welcome to the... Edinboro Arcade!", True, (255, 255, 255))
		self.fontX = (self.width - self.text.get_width()) // 2
		self.fontY = (self.height - self.text.get_height()) // 2
		self.fontUp = True
		self.fontSet = False
		self.fontArrived = False
		self.fontDestination = 0
		
	'''
	// Precise method, which guarantees v = v1 when t = 1.
	float lerp(float v0, float v1, float t) {
	return (1 - t) * v0 + t * v1;
	}
	'''
	def Learp(self, v1, v2, t):
		print("""Inside learp.
		v1 is: %s
		v2 is: %s
		t is: %s""" %(v1, v2, t))
		pos = (1 - t) * v1 + t * v2
		print("pos is: %s" %pos)
		
		return pos
		
		
	'''IM DEBATING HAVING THE TEXT FADE IN AND OUT.
	LOOKING AT THIS TO GET AN IDEA OF WHAT THAT WOULD LOOK LIKE.
	
	import pygame as pg


def main():
    clock = pg.time.Clock()
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 64)
    blue = pg.Color('royalblue')
    orig_surf = font.render('Enter your text', True, blue)
    txt_surf = orig_surf.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        if alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            alpha = max(alpha-4, 0)
            txt_surf = orig_surf.copy()  # Don't modify the original text surf.
            # Fill alpha_surf with this color to set its alpha value.
            alpha_surf.fill((255, 255, 255, alpha))
            # To make the text surface transparent, blit the transparent
            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

        screen.fill((30, 30, 30))
        screen.blit(txt_surf, (30, 60))
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
	'''
	def Move(self):
		if self.fontUp == True and self.fontSet == False:
			self.fontDestination = self.fontY - 10
			self.fontSet = True
			self.fontArrived = False
		elif self.fontSet == False:
			self.fontDestination = self.fontY + 10
			self.fontSet = True
			self.fontArrived = False
			
		if not self.fontArrived:
			self.menu = pygame.transform.scale(pygame.image.load(self.background).convert_alpha(), (1400, 1024))
			self.menuRect = self.menu.get_rect()
			self.screen.blit(self.menu, self.menuRect)
			
			self.fontY = self.fontY + self.Learp(self.fontY, self.fontDestination, abs(self.fontDestination - self.fontY))
			print(self.fontY)
			
			self.screen.blit(self.text, (self.fontX, self.fontY))
			pygame.display.flip()
			
			
			if self.fontY == self.fontDestination:
				self.fontArrived = True
				self.fontUp = False
				self.fontSet = False
		
	def Draw(self):
		#self.screen.fill((0,0,0))
		self.menu = pygame.transform.scale(pygame.image.load(self.background).convert_alpha(), (1400, 1024))
		self.menuRect = self.menu.get_rect()
		self.screen.blit(self.menu, self.menuRect)
		self.screen.blit(self.text, (self.fontX, self.fontY))
		'''
		self.menu = pygame.transform.scale(pygame.image.load(self.background).convert_alpha(), (1400, 1024))
		self.menuRect = self.menu.get_rect()
		self.screen.blit(self.menu, self.menuRect)
		'''
		
		pygame.display.flip()