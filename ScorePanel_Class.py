import pygame as pg
from settings import *


class ScorePanel:
    def __init__(self, window, basket):
        self.window = window
        self.basket = basket

    def draw(self):
        # pg.init()
        myfont = pg.font.SysFont("Arial", 40)
        score_board = myfont.render(f"Goals: {self.basket.score}", 1, (0, 0, 0))
        self.window.blit(score_board, (50, 60))