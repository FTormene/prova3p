import pygame, sys
from pygame.locals import *


pygame.init()


schermo=pygame.display.set_mode((600,400))

pygame.display.set_caption('disegni')
        
clock=pygame.time.Clock
fps=60

schermo.fill((255,255,255))
schermo1=pygame.display.set_mode((300, 300))
schermo1.fill((50,50,50))

schermo2=pygame.display.set_mode((300, 300))
schermo2.fill((0,0,0))



#pygame.display.flip()

clock.tick(fps)
while True:
    
    # inputs
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()

    
    clock.tick(fps)

    