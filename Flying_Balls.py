import pymunk
from settings import *


class FlyingBall:
    def __init__(self, space, ball_type='beat', vector=None):
        self.ball_type = ball_type
        self.space = space

        if self.ball_type == 'beat':
            self.create_ball(30, 5, RED, (100, 600))
            impulse_force_scalar = vector.length * 15
            impulse_force = (-1 * impulse_force_scalar * vector.impulse_x_y_ratio
                             , impulse_force_scalar * (1 / vector.impulse_x_y_ratio))
            self.beat_ball((0, 0), impulse_force)
        else:
            self.create_ball(30, 0.3, BLUE, (100, 100))

        self.previous_position = self.body.position

    def create_ball(self, radius, mass, color, position):
        self.body = pymunk.Body()
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.mass = mass
        self.shape.color = color + (100, )
        self.shape.elasticity = 0.1
        self.shape.friction = 0.5
        self.space.add(self.body, self.shape)

        return self.shape

    def beat_ball(self, impulse_direction, impulse_force):
        self.body.apply_impulse_at_local_point(impulse_force, impulse_direction)


class BallManager:
    def __init__(self, space):
        self.space = space
        self.ball_list = []
        self.beat_ball_list = []

    def create_balls(self):
        pass