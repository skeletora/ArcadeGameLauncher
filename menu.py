from GameButton import GameButton
import collections as col
import sys, pygame

class Menu:

    def __init__(self, screen, imageNames):
        self.screen = screen
        self.ON_SCREEN = 5
        self.width, self.height = pygame.display.get_surface().get_size()
        self.bNames = imageNames
        self.buttons = self.InitButtons(imageNames)
        self.cursor = 0


    def InitButtons(self, names):

        buttons = col.deque()
        for i in range(self.ON_SCREEN):
            buttons.append(GameButton(self.bNames[i]))
            buttons[-1].Move(612*(i-.5), self.height/4)

        return buttons


    def Rotate(self, x):
        for b in self.buttons:
            b.Move(x)

        if self.buttons[0].pos[0]+1024 < 0:
            self.cursor = (self.cursor + 1) % len(self.bNames)
            self.buttons.popleft()
            self.buttons.append(GameButton(self.bNames[(self.cursor + self.ON_SCREEN-1) % len(self.bNames)]))
            self.buttons[-1].Move(self.buttons[-2].pos[0]+612, self.height/4)


        elif self.buttons[-1].pos[0]-512 > self.width:
            self.cursor = (self.cursor - 1) % len(self.bNames)
            self.buttons.pop()
            self.buttons.appendleft(GameButton(self.bNames[self.cursor]))
            self.buttons[0].Move(self.buttons[1].pos[0]-612,self.height/4)



    def Draw(self):
        self.screen.fill((255, 255, 255))

        for i in self.buttons:
            self.screen.blit(i.img, i.pos)
        pygame.display.flip()