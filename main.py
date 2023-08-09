import maze
import player
import ray
import scene
import constants
import math
import pygame
import sys
import app

if __name__ == "__main__":
    pygame.init()
    app = app.App()
    while True:
        app.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

