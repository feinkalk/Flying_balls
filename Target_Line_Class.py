import pygame as pg
from settings import *
import math


class TargetVector:
    def __init__(self, window):
        self.window = window
        self.start_point = list(BEAT_BALL_START)
        self.movable_point = [400, 400]
        self.angle = 45
        self.length = 100
        self.impulse_x_y_ratio = 0.5

    def change_direction(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if self.angle <= 85:
                self.angle += 1
        if keys[pg.K_DOWN]:
            if 5 <= self.angle:
                self.angle -= 1
        if keys[pg.K_LEFT]:
            self.length -= 5
        if keys[pg.K_RIGHT]:
            self.length += 5

        # print(f"target angle is {self.angle}")

    def draw(self):
        self.movable_point = (math.cos(math.radians(self.angle)) * self.length + BEAT_BALL_START[0]
                              , BEAT_BALL_START[1] - math.sin(math.radians(self.angle)) * self.length)
        pg.draw.line(self.window, RED, tuple(self.start_point), tuple(self.movable_point))
        self.calculate_x_y_ratio()

    def calculate_x_y_ratio(self):
        self.impulse_x_y_ratio = (self.movable_point[0] - self.start_point[0]) / \
                                 (self.movable_point[1] - self.start_point[1])


