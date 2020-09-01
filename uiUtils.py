import time

import autoit

from constants import icon_tables_e, icon_checksums_e, Icons, pos_tables, Positions
from skillAction import *
from tapping import tapMenuFullExit


def CoordFromTuple(tuple):
    return tuple[0], tuple[1], tuple[2], tuple[3]

# def IsOpenBottomMenu(pos_str):
#     icon = icon_tables_e[pos_str]
#     icon_check_sum = icon_checksums_e[pos_str]
#
#     print(f'x icon checksum, {icon}, {pos_str})
#     x, y, x1, y1 = CoordFromTuple(icon)
#     checksum = autoit.pixel_checksum(x, y, x1, y1)
#     print(f'x icon checksum, {checksum}')
#
#     return checksum == icon_check_sum

def IsExistIcon(pos_str):
    icon = icon_tables_e[pos_str]
    icon_check_sum = icon_checksums_e[pos_str]

    print(f'x icon checksum, {icon}', {pos_str})
    x, y, x1, y1 = icon
    checksum = autoit.pixel_checksum(x, y, x1, y1)
    print(f'x icon checksum, {checksum}')

    return checksum == icon_check_sum

def IsOpenBottomMenuFull():
    return IsExistIcon(Icons.Bottom_Menu_X_Full.name)

def IsOpenBottomMenuHalf():
    return IsExistIcon(Icons.Bottom_Menu_X_Half.name)


def bottomMenuExitFull():
    # Bug: temp :  checksum is changing whenever restart LDPlayer.
    #if IsOpenBottomMenuFull():
    tapMenuFullExit()


def bottomMenuExitHalf():
    if IsOpenBottomMenuHalf():
        tapMenuFullExit()

def bottomMenuExit():
    bottomMenuExitHalf()
    bottomMenuExitFull()




# bottom menu
def openBMenu(menu):
    x, y, _, _ = icon_tables_e[menu]
    autoit.mouse_click('left', x, y, 1, 10)
    time.sleep(0.6)

    menuMakeFull()


def menuMakeFull():

    if IsExistIcon(Icons.Menu_Make_FUll.name):
        x, y, _, _ = icon_tables_e[Icons.Menu_Make_FUll.name]
        autoit.mouse_click('left', x, y, 1, 10)
        time.sleep(1)


# menu opearation
def menuScrollUp():
    x, y = pos_tables[Positions.BMenuWheel.name]
    autoit.mouse_move(x, y)
    autoit.mouse_wheel('up', 2)
    # caution: must put delay to work wheel up
    time.sleep(0.6)


def turnPlayScreen():
    # check Relics Icon on play screen
    # 36, 686 0xf3320c
    x, y = pos_tables[Positions.RelicsOnPlayScr.name]
    color = autoit.pixel_get_color(x, y)
    if color < 0xf00000:
        # clear all poped up layered windows
        bottomMenuExit()
        time.sleep(0.2)
        bottomMenuExit()
