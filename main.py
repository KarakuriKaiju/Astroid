# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# Remove this line since database.py doesn't exist
# from database import connect_database, database_version
from constants import *
from player import Player

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        #sets the FPS to 60FPS
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()