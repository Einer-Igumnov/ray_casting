import maze
import constants
import math
import scene
import pygame


class Ray:
    def __init__(self, _beg_x: float, _beg_y: float, _angle: float, _maze: maze.Maze):
        self.beg_x = _beg_x
        self.beg_y = _beg_y
        self.pos_x = _beg_x
        self.pos_y = _beg_y
        self.angle = _angle
        self.maze = _maze
        self.len = 0.0
        self.end_x = 0.0
        self.end_y = 0.0

    def move(self):
        self.pos_y += math.sin(self.angle) * constants.RAY_SPEED
        self.pos_x += math.cos(self.angle) * constants.RAY_SPEED

    def get_dist(self, player_angle: float):
        result = 0.0
        while self.maze.tile_is_empty(self.maze.get_tile(self.pos_x, self.pos_y)[1],
                                      self.maze.get_tile(self.pos_x, self.pos_y)[0]):
            self.move()
            result += constants.RAY_SPEED

        result *= math.cos(player_angle - self.angle)
        self.len = result
        self.end_x = self.pos_x
        self.end_y = self.pos_y


    def draw(self, win: scene.Scene):
        pygame.draw.line(win.window, (255, 0, 0), [self.beg_x, self.beg_y], [self.end_x, self.end_y], 3)

    def __del__(self):
        # print(self.len)
        ...

