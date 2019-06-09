import pygame
class Bomb(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite().__init__(self)
        self.isHidden = True
        self.color = color
        self.image = pygame.image.load(r'assets/empty.gif')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]