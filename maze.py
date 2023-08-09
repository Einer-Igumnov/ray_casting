import constants
import math
import scene
import pygame


class Maze:
    def __init__(self, _maze):
        self.maze = _maze
        self.n = len(_maze)
        self.m = len(_maze[0])

    def get_tile(self, _pos_x: float, _pos_y: float):
        return [math.floor(_pos_y / constants.TILE_SIZE), math.floor(_pos_x / constants.TILE_SIZE)]

    def tile_is_empty(self, pos_x: int, pos_y: int):
        try:
            if self.maze[pos_x][pos_y] == 1:
                return False
            else:
                return True
        except:
            return False

    def draw(self, win: scene.Scene):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.tile_is_empty(i, j):
                    ...
                else:
                    pygame.draw.rect(win.window, (100, 35, 200), (i * constants.TILE_SIZE + constants.TILE_SIZE / 8,
                                                                  j * constants.TILE_SIZE + constants.TILE_SIZE / 8,
                                                                  constants.TILE_SIZE - constants.TILE_SIZE * 2 / 8,
                                                                  constants.TILE_SIZE - constants.TILE_SIZE * 2 / 8))
