import sys
import pygame
from tree import RecursiveTree

pygame.init()
window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Fractal Tree")

tree1 = RecursiveTree(window_size[0]/2, window_size[1]-1, (127, 127, 127), 14, 200, 5)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            tree1.age += 1

    tree1.grow()
    tree1.display(screen)
    pygame.display.flip()
    clock.tick(60)
