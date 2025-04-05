
import pygame as pg

FPS = 32

SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511

game_image = {}
game_audio = {}

player_img = 'image/bird.png'
bg_img = 'images/background/png'
pipe_img = 'images/pipe.png'

display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
play_ground = SCREEN_HEIGHT * 0.8

time_clock = pg.time.Clock()