import math
import pygame as pg
import pymunk
import pymunk.pygame_util
from settings import *
from Flying_Balls import *
from Target_Line_Class import *
from Basket_Class import *
from ScorePanel_Class import *


pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))

vector = None


def calculate_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])


def draw(space, window, draw_options, target_line, score_panel):
    window.fill("white")
    space.debug_draw(draw_options)

    if vector is not None:
        pg.draw.line(window, RED, vector[0], vector[1])
    # pg.draw.circle(window, BLACK, (280, 630), 10)

    target_line.draw()
    score_panel.draw()
    pg.display.update()


def create_boundaries(space, width, height):
    rects = [
        [(500, 700), (1000, 20)],
        [(20, 400), (40, 800)],
        [(980, 400), (40, 800)],
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.5
        shape.friction = 0.5
        space.add(body, shape)


def create_lines(space):
    lines = [
        [(0, 100), (200, 130)]
    ]

    for start, end in lines:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, start, end, 5)
        shape.elasticity = 0.7
        shape.friction = 0.9
        space.add(body, shape)


def run_func(window, width, height):
    run = True
    clock = pg.time.Clock()
    ball_list = []
    beat_ball_list = []
    time_elapsed_since_last_action = 0

    # create objects
    space = pymunk.Space()
    space.gravity = (0, 981)
    target_line = TargetVector(window)
    basket = Basket(space)
    ball_manager = BallManager(space)
    create_boundaries(space, 100, 100)
    score_panel = ScorePanel(window, basket, ball_manager)
    create_lines(space)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

            if event.type == pg.KEYDOWN and event.key == pg.K_LALT:
                beat_ball_list.append(FlyingBall(space, ball_type='beat', vector=target_line))

        ball_manager.create_balls(max_number=10)
        ball_manager.remove_excess_balls()
        basket.check_goal(ball_list)

        # draw and tick
        basket.move()
        target_line.change_direction()
        draw(space, window, draw_options, target_line, score_panel)
        space.step(DT)
        time_elapsed_since_last_action += clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    run_func(window, WIDTH, HEIGHT)

# if event.type == pg.MOUSEBUTTONDOWN:
#     for ball in ball_list:
#         impulse_direction = (100, 0)
#         impulse_force = (200, 200)
#
#         ball.beat_ball(impulse_direction, impulse_force)
#
#         line_start = (int(ball.body.position[0] + impulse_direction[0]),
#                       int(ball.body.position[1] - impulse_direction[1]))
#
#         line_end = (int(ball.body.position[0] + impulse_direction[0] + impulse_force[0]),
#                     int(ball.body.position[1] - impulse_direction[1]) - impulse_force[1])
#         global vector
#         vector = (line_start, line_end)