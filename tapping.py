import time

import autoit

click_coord_table = \
    {
        'tapping': (310, 525),
        'pet': (335, 510),
        'petburst': (285, 455),
        'clanmate': (215, 545),
        'menufullexit': (561, 44),
        'menuharfexit': (525, 595),
        'fairystart': (80, 280),
        'fairyend': (580, 280),
        'fairycollect': (500, 774),


    }


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
    for d in daggers:
        autoit.mouse_click('left', d[0], d[1], 3, 10)
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

def _tapCursor():
    autoit.mouse_down('left')
    autoit.mouse_up('left')
