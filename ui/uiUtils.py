import time

from data.constants import icon_tables_e, icon_checksums_e, Icons, pos_tables, Positions, click_coord_table
from opencv.btnDetect import IsExistBtn
from skillAction import *
from tapping import tapMenuFullExit
from utils import IsColorAtCoord


def _tap(pos_str):
    x, y = click_coord_table[pos_str]
    autoit.mouse_click("left", x, y, 1, 3)

def tap(x,y):
    autoit.mouse_click("left", x, y, 1, 3)


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


def IsExistIcon(ImageEnum):

    return IsExistBtn(ImageEnum)

    # icon = icon_tables_e[pos_str]
    # icon_check_sum = icon_checksums_e[pos_str]
    #
    # print(f'x icon checksum, {icon}', {pos_str})
    # x, y, x1, y1 = icon
    # checksum = autoit.pixel_checksum(x, y, x1, y1)
    # print(f'x icon checksum, {checksum}')
    #
    # return checksum == icon_check_sum




# menu opearation
def menuScrollUpLong():
    x, y = pos_tables[Positions.BMenuWheel.name]
    # autoit.mouse_move(x, y)
    # autoit.mouse_down('left')
    # autoit.mouse_move(x, y+500)
    # autoit.mouse_up(x,y+500)
    autoit.mouse_click_drag(x,y,x,y+700,'left', 7)
    # autoit.mouse_wheel('up', 2)
    # caution: must put delay to work wheel up
    time.sleep(0.6)


# menu opearation
def menuScrollUp():
    x, y = pos_tables[Positions.BMenuWheel.name]

    # autoit.mouse_down('left')
    autoit.mouse_click_drag(x, y, x, y +700)

    # autoit.mouse_move(x, y)
    # autoit.mouse_wheel('up', 2)
    # # autoit.mouse_wheel('up', 2)
    # # caution: must put delay to work wheel up
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

def turnOnBossBattle():
    # check boss battle box
    # 510, 95, 0x3c4a4d : boss engaging.
    # 0xef5b10 : fight boss btn color
    x = 510
    y = 95
    # c = autoit.pixel_get_color(510, 95)
    if IsColorAtCoord(x, y, 0xef5b10, offset=0x2):
        autoit.mouse_click('left', x, y, 1, 10)


# check boss timer bar
# ret : True : slow down state
def checkSlowDown(mode='SCPorter'):
    # bar = 423, 138 ==>  x: 190
    # 400 : SC porter -> SC push
    BossTimerBar_Endx = 423
    BossTimerBar_Endy =  138
    BossTimerBar_Beginx = 190
    BossTimerBar_SCPorter_Limit = 400
    BossTimerBar_SCPush_Limit = 200

    # check is there timer?
    if 0xffffff != autoit.pixel_get_color(159, BossTimerBar_Endy):
        return False

    # get current position of the timer bar
    cur_bar_x = 0
    for x in range(BossTimerBar_Endx, BossTimerBar_Beginx, -1):
        c = autoit.pixel_get_color(x, BossTimerBar_Endy)
        if c == 0xffffff:
            cur_bar_x = x
            break

    print(f' Slow down : chechk boss timer bar ', {cur_bar_x})
    # check if it is slow down state
    if mode == 'SCPorter' and cur_bar_x < BossTimerBar_SCPorter_Limit:
        return True
    elif mode == 'SCPush' and cur_bar_x < BossTimerBar_SCPush_Limit:
        return True

    return False



