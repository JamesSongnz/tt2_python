'''
    lv up latest heroes
'''
import time

import autoit

from constants import hero_btn_init_y, hero_btn_x, hero_btn_activated_check_y, CR_HeroEleTypes, HeroEleType
from uiUtils import bottomMenuExitFull, Icons, openBMenu, menuScrollUp, bottomMenuExit

import enum

from utils import IsColorInRect

''' 
class BMenus(enum.Enum):
    Tap = enum.auto()
    Heroes = enum.auto()
    Equip = enum.auto()
    Pet = enum.auto()
'''


hero_type = HeroEleType.Spell


def heroLeveling():
    global hero_type
    print(f'Hero lv up')

    # open bottom menu
    bottomMenuExit()
    openBMenu(Icons.BMenu_Heroes.name)

    # check activated btn
    # click lv up btn
    hero_type = getHeroType()

    # 480 - 210  / 5 :    - distance due to addition first in the loop
    if not checkActivatedHeroBtn():
        bottomMenuExit()
        return

    # scroll up
    menuScrollUp()

    # click lv up btn
    distance_btn_y = 85
    # 480 - 210  / 5 :    - distance due to addition first in the loop
    y = hero_btn_init_y - distance_btn_y
    for i in range(6):
        y += distance_btn_y
        color = autoit.pixel_get_color(hero_btn_x, y)
        # skip in case not activated
        if color < 0xe00000:
            continue

        for j in range(4):
            autoit.mouse_click('left', hero_btn_x, y, 1, 3)
            time.sleep(0.1)

    bottomMenuExit()


def checkActivatedHeroBtn():
    y = hero_btn_activated_check_y
    while y < 590:
        y += 30
        color = autoit.pixel_get_color(hero_btn_x, y)
        # skip in case not activated
        if color > 0xe00000:
            return True
    return False

def getHeroType():
    x = 368
    y = 281

    for key, color in CR_HeroEleTypes.items():
        if IsColorInRect(x, y, color, 4, 6):
            return key

    return None