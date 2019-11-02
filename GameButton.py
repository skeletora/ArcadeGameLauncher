import pygame

class GameButton:

    def __init__(self, img):
        self.img = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (512, 512))
        self.pos = self.img.get_rect()

    def Move(self, x=0, y=0):
        self.pos = self.pos.move([x, y])


    def CheckClicked(self, local):
        clicked = False

        if self.pos[0]+self.pos[2] > local[0] > self.pos[0]:
            if self.pos[1] + self.pos[3] > local[1] > self.pos[1]:
                clicked = True

        return clicked