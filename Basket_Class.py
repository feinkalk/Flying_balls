import pygame as pg
import pymunk
from settings import *


class Basket:
    def __init__(self, space):
        self.space = space
        self.score = 0
        self.is_moving = True
        self.moving_right = True
        self.shape_list = []
        self.create_boundaries()

    def create_boundaries(self):
        self.width = BASKET_WIDTH
        self.height = BASKET_HEIGHT
        self.wall = BASKET_WALL
        self.position = BASKET_INITIAL_POSITION

        rects = [
            [(self.position[0] - self.width / 2 + self.wall / 2, self.position[1]), (self.wall, self.height)],
            [(self.position[0], self.position[1] + self.height / 2 - self.wall / 2, ), (self.width, self.wall)],
            [(self.position[0] + self.width / 2 - self.wall / 2, self.position[1]), (self.wall, self.height)],
        ]

        for pos, size in rects:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
            self.body.position = pos
            self.shape = pymunk.Poly.create_box(self.body, size)
            self.shape.elasticity = 0.5
            self.shape.friction = 0.5
            self.space.add(self.body, self.shape)
            self.shape_list.append(self.shape)

    def check_goal(self, ball_list):
        for index, ball in enumerate(ball_list):
            if (self.position[0] - self.width * 0.4 < ball.body.position[0] < self.position[0] + self.width / 2 and
                self.position[1] - self.height / 3 < ball.body.position[1] < self.position[1] + self.height / 2):

                self.score += 1
                self.space.remove(ball.shape, ball.body)
                del ball_list[index]

    def move(self):
        x_start = BASKET_INITIAL_POSITION[0]
        x_end = BASKET_INITIAL_POSITION[0] + BASKET_MOVING_RANGE

        if self.is_moving:
            if self.moving_right:
                if self.body.position[0] + BASKET_MOVING_SPEED > x_end:
                    self.moving_right = False
                self.single_move(BASKET_MOVING_SPEED)
            else:
                if self.body.position[0] - BASKET_MOVING_SPEED < x_start:
                    self.moving_right = True
                self.single_move(-1 * BASKET_MOVING_SPEED)

    def single_move(self, velocity):
        for shape in self.shape_list:
            shape.body.position = (int(shape.body.position[0] + velocity)
                                   , int(shape.body.position[1]))
