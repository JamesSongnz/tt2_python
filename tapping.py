import time

import autoit

click_coord_table = \
    {
        'tapping': (310, 525),
        'pet': (335, 510),
        'clanmate': (215, 545),
        'menufullexit': (525, 55),
        'menuharfexit': (525, 595),


    }

def tapping():
    for i in range(20):
        _tap('tapping')
        time.sleep(0.05)


# activate clanmate
def tapClanmate():
    _tap('clanmate')

# pet money
def tapPetMoney():
    _tap('pet')

#
def tapMenuFullExit():
    _tap('menufullexit')


def _tap(pos_str):
    x, y = click_coord_table[pos_str]
    autoit.mouse_click("left", x, y, 1, 10)


