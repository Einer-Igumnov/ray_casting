import math
import ray
import maze
import scene
import pygame
import scene


class Player:
    def __init__(self, _pos_x: float, _pos_y: float):
        self.pos_x = _pos_x
        self.pos_y = _pos_y
        self.speed = 2.0
        self.angle = 0.0

    def rotate(self, delta_ang):
        self.angle = self.angle + 2 * delta_ang
        if self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi

    def move(self, _maze: maze.Maze):
        new_y = self.pos_y + math.sin(self.angle) * self.speed
        new_x = self.pos_x + math.cos(self.angle) * self.speed
        if _maze.tile_is_empty(_maze.get_tile(new_x, new_y)[1],
                               _maze.get_tile(new_x, new_y)[0]):
            self.pos_x = new_x
            self.pos_y = new_y

    def get_view(self, _maze: maze.Maze, win: scene.Scene):
        ang = self.angle - 1 / 3 * math.pi
        result = []
        while ang < self.angle + 1 / 3 * math.pi:
            now_ray = ray.Ray(self.pos_x, self.pos_y, ang, _maze)
            now_ray.get_dist(self.angle)
            now_ray.draw(win)
            result.append(now_ray.len)
            del now_ray
            ang += math.pi / 90.0 / 8
        return result

    def draw(self, win: scene.Scene):
        pygame.draw.circle(win.window, (0, 0, 255), (self.pos_x, self.pos_y), 4)
