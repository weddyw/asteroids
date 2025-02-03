# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import random
# imports in the constants.py and the * imports the whole file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from asteroid import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()  # stores into variable
    dt = 0
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
            colliding_shots = pygame.sprite.spritecollide(asteroid, shots, False)
            if colliding_shots:
                asteroid.split()
                for shot in colliding_shots:
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # divides the return by 1000 to convert to milliseconds


if __name__ == "__main__":
    main()