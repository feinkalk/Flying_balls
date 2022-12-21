import pygame as pg
from Flying_Balls import *
from settings import *


class ScorePanel:
    def __init__(self, window, basket, ball_manager: BallManager):
        self.window = window
        self.basket = basket
        self.ball_manager = ball_manager

    def draw(self):
        # pg.init()
        if not self.ball_manager.game_over:
            myfont = pg.font.SysFont("Arial", 40)
            score_board = myfont.render(f"Goals: {self.basket.score}", 1, (0, 0, 0))
            self.window.blit(score_board, (50, 60))
        else:
            myfont = pg.font.SysFont("Arial", 60)
            score_board = myfont.render(f" Game over!. You scored goals: {self.basket.score}", 1, (0, 0, 0))
            self.window.blit(score_board, (150, 400))