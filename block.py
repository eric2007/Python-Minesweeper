import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        #0:default 1:dig 2:flag 3:explode
        self.state = 0
        self.image = pygame.image.load(r'assets\block.jpg')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def dig(self):
        self.image = pygame.image.load(r'assets\block dig.jpg')
        self.state = 1