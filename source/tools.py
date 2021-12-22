import os
import constants as C
import pygame as pg


class Game:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()

    def run(self,state):
        while True:

            state.update(self.screen)

            pg.display.update()
            self.clock.tick(60)


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics


load_graphics("C:/Users/MyPC/PycharmProjects/mygame/resources/graphics")
