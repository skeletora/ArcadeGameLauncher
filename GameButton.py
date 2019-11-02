import pygame

class GameButton:

    def __init__(self, img, music=None):
        self.img = pygame.transform.scale(pygame.image.load(img), (512, 512))
        self.pos = self.img.get_rect()
        self.music = music

    def Move(self, x=0, y=0):
        self.pos = self.pos.move([x, y])

