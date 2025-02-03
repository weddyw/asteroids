# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# imports in the constants.py and the * imports the whole file
from constants import *


def main():
    pygame.init()
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()