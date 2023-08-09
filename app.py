import maze
import player
import ray
import scene
import constants
import math
import pygame
import sys
import time


class App:
    def __init__(self):
        self.maze = None
        self.player = None
        input_maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        self.maze = maze.Maze(input_maze)
        self.scene = scene.Scene()
        self.maze.draw(self.scene)
        self.player = player.Player(24.0, 24.0)

    def draw_map(self):
        self.maze.draw(self.scene)
        self.player.get_view(self.maze, self.scene)
        self.player.draw(self.scene)

    def draw_3d(self):
        pygame.draw.rect(self.scene.window, (50, 50, 50), (0, 400, 1200, 800))
        dists = self.player.get_view(self.maze, self.scene)
        for i in range(len(dists)):
            height = constants.WALL_HEIGHT / dists[i]
            color = 200 * (120 - dists[i]) / 120
            pygame.draw.rect(self.scene.window, (color, color, color), ((i-1)*1200 / len(dists), (800-height) / 2, 1*1200 / len(dists) + 3, height))

    def update(self):
        keys = pygame.key.get_pressed()
        delta = (pygame.mouse.get_pos()[0] - 600) * 0.0003
        # self.player.rotate(delta)
        # pygame.mouse.set_pos(600, 400)
        if keys[pygame.K_LEFT]:
            self.player.rotate(- math.pi / 90.0)
        if keys[pygame.K_RIGHT]:
            self.player.rotate(math.pi / 90.0)
        if keys[pygame.K_w]:
            self.player.move(self.maze)
        self.scene.window.fill((0, 0, 0))
        self.draw_3d()
        self.draw_map()


