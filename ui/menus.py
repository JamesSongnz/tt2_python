import time

from autoit import autoit

from data.Point import Point
from data.constants import Icons, icon_tables_e
from data.coordinates import Icons_coord, Image_coords
from data.utils import ratioConvertIcon
from ui import uiAction
from ui.uiAction import clickPoint, click, clickIcon, mouseOut
from ui.uiUtils import IsExistIcon


def IsOpenBottomMenuFull():
    return IsExistIcon(Image_coords.Bottom_Menu_X_Full)

def IsOpenBottomMenuHalf():
    return IsExistIcon(Image_coords.Bottom_Menu_X_Half)


def bottomMenuExitFull():
    # Bug: temp :  checksum is changing whenever restart LDPlayer.
    if IsOpenBottomMenuFull():
        clickIcon(Icons_coord.IPanel_Full_x)


def bottomMenuExitHalf():
    if IsOpenBottomMenuHalf():
        clickIcon(Icons_coord.IPanel_Half_x)


# bottom menu
def bottomMenuExit():
    bottomMenuExitHalf()
    bottomMenuExitFull()
    uiAction.mouseOut()


def openBtMenu(menu_icon):
    k = menu_icon.sk
    if k:
        uiAction.press(k)
    else:
        x, y = menu_icon.pos
        click(x, y)

    time.sleep(0.5)

    menuMakeFull()


def menuMakeFull():

    if IsOpenBottomMenuHalf():
       clickIcon(Icons_coord.IPanel_Make_Full)


