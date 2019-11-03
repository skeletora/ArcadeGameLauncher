import pygame

class MenuButton:

    def __init__(self, game, length, width):
        self.game = game
        self.img = pygame.transform.scale(pygame.image.load(game.image).convert_alpha(), (length, width))
        self.pos = self.img.get_rect()

    def Move(self, x=0, y=0):
        self.pos = self.pos.move([x, y])


    def CheckClicked(self, local):
        clicked = False

        if self.pos[0]+self.pos[2] > local[0] > self.pos[0]:
            if self.pos[1] + self.pos[3] > local[1] > self.pos[1]:
                clicked = True

        return clicked