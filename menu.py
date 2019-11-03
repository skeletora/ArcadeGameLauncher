from GameButton import GameButton
import collections as col
import sys, pygame

LAUNCHERPATH="C:\Launcher"

class Menu:


    def __init__(self, screen, games):
        self.screen = screen
        self.ON_SCREEN = 5
        self.width, self.height = pygame.display.get_surface().get_size()
        self.background = LAUNCHERPATH + '\darkenedbackground.png'
        self.menu = pygame.transform.scale(pygame.image.load(self.background).convert_alpha(), (self.width, self.width))


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


    def Rotate(self, x):
        for b in self.buttons:
            b.Move(x)

        if self.buttons[0].pos[0]+1024 < 0:
            self.cursor = (self.cursor + 1) % len(self.bNames)
            self.buttons.popleft()
            self.buttons.append(GameButton(self.gameList.gamesList[(self.cursor + self.ON_SCREEN-1) % len(self.bNames)]))
            self.buttons[-1].Move(self.buttons[-2].pos[0]+612, self.height/4)

        elif self.buttons[-1].pos[0]-512 > self.width:
            self.cursor = (self.cursor - 1) % len(self.bNames)
            self.buttons.pop()
            self.buttons.appendleft(GameButton(self.gameList.gamesList[self.cursor]))
            self.buttons[0].Move(self.buttons[1].pos[0]-612,self.height/4)


    def Draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.menu, (0,0))

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