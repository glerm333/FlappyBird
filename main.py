import random as r
import pygame as pg

import sys

from config import *
from functions import *

# from pygame.local import *

if __name__ == "__main__":

    pg.init()

    pg.display.set_caption("FluppyBird")

    game_image['numbers'] = (
        pg.image.load('images/0.png').convert_alpha(),
        pg.image.load('images/1.png').convert_alpha(),
        pg.image.load('images/2.png').convert_alpha(),
        pg.image.load('images/3.png').convert_alpha(),
        pg.image.load('images/4.png').convert_alpha(),
        pg.image.load('images/5.png').convert_alpha(),
        pg.image.load('images/6.png').convert_alpha(),
        pg.image.load('images/7.png').convert_alpha(),
        pg.image.load('images/8.png').convert_alpha(),
        pg.image.load('images/9.png').convert_alpha(),
    )
    game_image['message'] = pg.image.load('images/message.png').convert_alpha()
    game_image['base'] = pg.image.load('images/base.png').convert_alpha()
    game_image['pipe'] = (pg.transform.rotate(pg.image.load(pipe_img).convert_alpha(), 180), pg.image.load(pipe_img).convert_alpha())

    game_audio['die'] = pg.mixer.Sound('sounds/die.wav')
    game_audio['hit'] = pg.mixer.Sound('sounds/hit.wav')
    game_audio['point'] = pg.mixer.Sound('sounds/point.wav')
    game_audio['swoosh'] = pg.mixer.Sound('sounds/swoosh.wav')
    game_audio['wing'] = pg.mixer.Sound('sounds/wing.wav')

    game_image['player'] = pg.image.load('images/bird.png')
    game_image['background'] = pg.image.load('images/background.png')

    while True:
        welcome_main_screen()
        main_gameplay()
