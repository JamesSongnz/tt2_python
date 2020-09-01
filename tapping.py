import time

import autoit

from constants import click_coord_table, CR_Dagger
from utils import IsColorAtCoord


def catchFairy():
    # swipe fairy line
    x, y = click_coord_table['fairystart']
    x2, _ = click_coord_table['fairyend']
    step  = 12
    offset = int((x2 - x ) / step)
    for i in range(step):
        autoit.mouse_click('left', x+i*offset, y, 1, 5)
        time.sleep(0.07)

        tapFairyCollect()

    # reverse
    for i in range(11, -1, -1):
        autoit.mouse_click('left', x + i*offset, y, 1, 5)
        time.sleep(0.07)
        tapFairyCollect()


    time.sleep(1)
    # move cursor
    _tap('fairycollect')



def posionDagger():
    daggers = [(160, 430), (218, 460), (258, 484), (300, 480), (343, 440), (360, 430)]
    # 177, 427

    # dagger color 4d7f24, 4a 84 29
    for d in daggers:
        # is there dagger?
        if IsColorAtCoord(d[0], d[1], CR_Dagger):
            autoit.mouse_click('left', d[0], d[1], 3, 10)
            # tap during 2s
            for i in range(40):
                tapCursor()
        #time.sleep(0.2)

def activateFS():
    for i in range(20):
        _tap('tapping')
        time.sleep(0.02)

def tapping():
    _tap('tapping')

def tapCursor():
    #for i in range(4):
    _tapCursor()
    time.sleep(0.04)


# activate clanmate
def tapClanmate():
    _tap('clanmate')

# pet money
def tapPetMoney():
    _tap('pet')

def tapFairyCollect():
    # collect check  500, 774, 0x289fcb
    cx, cy = click_coord_table['fairycollect']
    color = autoit.pixel_get_color(cx, cy)
    if 0x280000 < color and color < 0x28ffff:
        _tap('fairycollect')


# pet build burst
def tapPetBurst(sec):

    for i in range(sec):
        for j in range(20):
            _tap('petburst')
            time.sleep(0.02)
#
def tapMenuFullExit():
    _tap('menufullexit')


def _tap(pos_str):
    x, y = click_coord_table[pos_str]
    autoit.mouse_click("left", x, y, 1, 3)

def tap(x,y):
    autoit.mouse_click("left", x, y, 1, 3)


def _tapCursor():
    autoit.mouse_down('left')
    autoit.mouse_up('left')
