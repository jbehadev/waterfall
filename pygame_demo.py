import sys, pygame
from pygame.constants import QUIT
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

material_matrix = [range(320),range(240)]

for x in material_matrix:
    for y in material_matrix:
        y = 0

print(material_matrix)

pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
