import pygame as pg
import source.constants as C

class MainMenu:
    def __init__(self):
        pass
    def setup_background(self):
        self.background= C.GRAPHICS['menu']
        self.background_rect=self.background.get_rect()
        # self.background=pg.transform.scale(self.background,self.background_rect)
