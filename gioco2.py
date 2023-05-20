import pygame, sys

from pygame.locals import *
import random

pygame.init()

screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

fps=60
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
listapunti=[(1,20),(30,50),(70,90)]
listapunti2=[(1,40),(60,90),(100,120)]

    # Dimensioni di una cella del labirinto
CELL_SIZE = 40
CELLS_WIDE = 800 // CELL_SIZE
CELLS_HIGH = 600 // CELL_SIZE

# Colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


Rettangolo = pygame.Rect((0,0),(40,40))

line=pygame.Surface((50,50))
pygame.draw.lines((line), (red), (False), (listapunti))


for i in range(30):
    pygame.draw.lines((line), (red), (False), (listapunti2))

Immagine=pygame.Surface((40,40))
Immagine.fill(white)

grid = []
for i in range(CELLS_WIDE):
    grid.append([])
    for j in range(CELLS_HIGH):
        grid[i].append(True)

# Impostazione delle celle iniziali come vuote
start_x = random.randint(0, CELLS_WIDE - 1)
start_y = random.randint(0, CELLS_HIGH - 1)
grid[start_x][start_y] = False

# Funzione per disegnare il labirinto
def draw_maze():
    screen.fill(BLACK)

    for i in range(CELLS_WIDE):
        for j in range(CELLS_HIGH):
            if grid[i][j]:
                pygame.draw.rect(screen, BLACK, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys.exit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Rettangolo.move_ip(0,-5)
            elif event.key == pygame.K_s:
                Rettangolo.move_ip(0,5)
            elif event.key == pygame.K_a:
                Rettangolo.move_ip(-5,0)
            elif event.key == pygame.K_d:
                Rettangolo.move_ip(5,0)
    draw_maze()

    
    
    screen.fill(black)
    screen.blit(line,(40,40))
    screen.blit(Immagine,Rettangolo)
    
    pygame.display.update()
    #pygame.quit()