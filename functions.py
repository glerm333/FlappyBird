import sys

import pygame as pg
import random

from config import *


def welcome_main_screen():
    p_x = int(SCREEN_WIDTH / 5)
    p_y = int((SCREEN_HEIGHT - game_image['player'].get_height()) / 2)

    msg_x = int((SCREEN_WIDTH - game_image['message'].get_width()) / 2)
    msg_y = int(SCREEN_HEIGHT * 0.13)

    bg_x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and (event.key == pg.K_SPACE or event.key == pg.K_UP):
                return
            else:
                display.blit(game_image['background'], (0,0))
                display.blit(game_image['player'], (p_x,p_y))
                display.blit(game_image['message'], (msg_x,msg_y))
                display.blit(game_image['base'], (bg_x, bg_x))

                pg.display.update()
                time_clock.tick(FPS)

def main_gameplay():
    score = 0
    p_x = int(SCREEN_WIDTH / 5)
    p_y = int(SCREEN_HEIGHT / 2)
    bg_x = 0

    n_pipe1 = get_random_pipes()
    n_pipe2 = get_random_pipes()

    up_pipe=[
        {
            'x':SCREEN_WIDTH + 200,
            'y':n_pipe1[0]['y']
        },
        {
            'x':SCREEN_WIDTH + 200,
            'y':n_pipe2[0]['y']
        }
    ]
    low_pipe=[
        {
            'x':SCREEN_WIDTH + 200,
            'y':n_pipe1[1]['y']
        },
        {
            'x':SCREEN_WIDTH + 200,
            'y':n_pipe2[1]['y']
        }
    ]

    pip_Vx = -4

    p_vx = -9
    p_mvx = 10
    p_accuracy = -8

    p_flap_accuracy = -8
    p_flap = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and (event.key == pg.K_ESCAPE or event.key == pg.K_UP):
                if p_y > 0:
                    p_vx = p_flap_accuracy
                    p_flap = True
                    game_audio['wind'].play()
        cr_tst = is_Colliding(p_x, p_y, up_pipe, low_pipe)
        if cr_tst:
            return

        p_middle_positions = p_x + game_image["player"].get_width() / 2
        for pipe in up_pipe:
            pip_middle_position = pipe['x'] + game_image['pipe'][0].get_width() / 2

            if pip_middle_position <= p_middle_positions < pip_middle_position + 4:
                score += 1
                print("ваш счет:", score)
                game_audio['point'].play()

        if p_vx < p_mvx and not p_flap:
            p_vx += p_accuracy

        if p_flap:
            p_flap = False

        p_height = game_image['player'].get_height()
        p_y = p_y + min(p_vx, play_ground - p_y - p_height)

        for pip_upper, pip_lover in zip(up_pipe, low_pipe):
            pip_upper['x'] += pip_Vx
            pip_lover['x'] += pip_Vx

        if 0< up_pipe[0]['x'] < 5:
            new_pipe = get_random_pipes()
            up_pipe.append(new_pipe[0])
            low_pipe.append(new_pipe[1])

        display.blit(game_image['background'], (0,0))
        for pip_upper, pip_lover in zip(up_pipe, low_pipe):
            display.blit(game_image['pipe'][0], (pip_upper['x'], pip_upper['y']))
            display.blit(game_image['pipe'][1], (pip_lover['x'], pip_lover['y']))

            display.blit(game_image['base'], (bg_x, play_ground))
            display.blit(game_image['player'],(p_x,p_y))

            d = [int(x) for x in list(str(score))]
            w = 0
            for digdit in d:
                w += game_image['numbers'][digdit].get_width()
            Xoffset = (SCREEN_WIDTH - w) / 2

            for digdit in d:
                display.blit(game_image['numbers'][digdit], (Xoffset, SCREEN_HEIGHT * 0.12))
                Xoffset += game_image['numbers'][digdit].get_width()

            pg.display.update()
            time_clock.tick(FPS)

def get_random_pipes():
    pipe_h = game_image['pipe'][0].get_height()
    off_s = SCREEN_HEIGHT / 3
    yes2 = off_s + random.randint(0,int(SCREEN_HEIGHT - game_image['base'].get_height() - 1.2 * off_s))
    pipeX = SCREEN_WIDTH + 10
    y1 = pipe_h - yes2 + off_s
    pipes = [
        {'x':pipeX, 'y': -y1},
        {'x':pipeX, 'y': yes2}
    ]
    return pipes


def is_Colliding(p_x,p_y, up_pipes, low_pipes):
    if p_y > play_ground - 25 or p_y < 0:
        game_audio['hit'].play()
        return  True

    for pipe in up_pipes:
        pip_h = game_image['pipe'][0].get_height()
        if (p_y < pip_h + pipe['y'] and abs(p_x - pipe['x']) < game_image['pipe'][0].get_width ()):
            game_audio['hit'].play()
            return True

    for pipe in low_pipes:
        if(p_y + game_image['player'].get_height() > pipe['y']) and abs (p_x - pipe['x']) < \
                game_image['pipe'][0].get_width():
            game_audio['hit'].play()
            return True

    return False

