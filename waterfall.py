import pygame, sys
from pygame.constants import QUIT
from material_matrix import material_matrix
import numpy as N
pygame.init()
width = 40
height = 40

size = width, height
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

game_screen = material_matrix(width,height)

game_screen.set_material(4,4,255)

game_screen.set_material(30,30,255)

game_screen.print_matrix()

surf = pygame.surfarray.make_surface(game_screen.as_array())
screen.blit(surf, (0, 0))

pygame.display.flip()

pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


    
