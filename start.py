import sys
import time
try:
    import pygame
    from pygame.locals import *
    import stage
except ImportError:
    print('pygame not install(use \'pip install pygame to install\'')
    sys.exit(-1)
#level = input('Level(1, 2 and 3):')
#level_size = (())
pygame.init()
mystage = stage.Stage()
screen = pygame.display.set_mode([198,228])
mygroup = pygame.sprite.Group()
mygroup.add(mystage)
screen.fill((200,200,200))
clock = pygame.time.Clock()
pygame.display.set_caption('Mine Sweeper')
pygame.display.set_icon(pygame.image.load(r'assets\bomb.png'))
mystage.init()
#print(time.process_time())
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                x,y = pygame.mouse.get_pos()
                mystage.Rbutton(x,y)
            elif pygame.mouse.get_pressed() == (0,0,1):
                x,y = pygame.mouse.get_pos()
                mystage.Lbutton(x,y)
    clock.tick(24)
    mygroup.draw(screen)  
    mygroup.update()
    pygame.display.update()