import pygame
import time
import block
import random
class Stage(pygame.sprite.Sprite):
    blocks = []
    bombs = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'assets\empty.jpg')
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
    def init(self):
        time.sleep(0.05)
        # self.groups()[0].add(block.Block(18,18))
        for x in range(9,198,18):
            l1 = []
            for y in range(9,198,18):
                # print(not blocksState[x][y] & 0x10 == 0)
                l1.append(block.Block(x,y))
            self.blocks.append(l1)
        for x in range(10):
            for y in range(10):
                # print(not blodcksState[x][y] & 0x10 == 0)
                self.groups()[0].add(self.blocks[x][y])
        for _ in range(10):
            x = random.randint(0,9)
            y = random.randint(0,9)
            self.bombs[x][y] = 10
            if self.indexErr(x-1,y-1):
                self.bombs[x-1][y-1]+=1
            if self.indexErr(x-1,y):
                self.bombs[x-1][y]+=1
            if self.indexErr(x-1,y+1):
                self.bombs[x-1][y+1]+=1
            if self.indexErr(x,y-1):
                self.bombs[x][y-1]+=1
            if self.indexErr(x,y+1):
                self.bombs[x-1][y-1]+=1
            if self.indexErr(x+1,y-1):
                self.bombs[x-1][y-1]+=1
            if self.indexErr(x-1,y):
                self.bombs[x-1][y-1]+=1
            if self.indexErr(x-1,y+1):
                self.bombs[x-1][y-1]+=1
    def Lbutton(self,x,y):
        pass
    def Rbutton(self,x,y):
        posX = self.getPosByAxis(x)
        posY = self.getPosByAxis(y)
        if not(posX>0 or posX<10 or posY>10 or posY<10):
            return
        try:
            self.blocks[posX][posY].dig()
        except IndexError:
            pass
    def getPosByAxis(self,pos):
        return (pos-9)//18
    def indexErr(self,x,y):
          return not(x<0 or x>9 or y<0 or y>9)