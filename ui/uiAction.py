import time

import pyautogui
from autoit import autoit

from data.Point import Point
from data.coordinates import Icons_coord


def clickPoint(p: Point):
    autoit.mouse_click('left', p.x, p.y, 1, 10)

def click(x,y):
    autoit.mouse_click('left', x, y, 1, 10)


def clickMultiple(icon, n=20, delay=0.1):
    x, y = icon.pos
    # clickMultipleXY(x, y, n, delay)
    for i in range(0,20):
        click(x,y)
        time.sleep(delay)

def clickMultipleXY(x, y, n=10, delay=0.1):
    pyautogui.click(x, y, clicks=n, interval=delay)



def clickIcon(icon, delay=0.6):
    x, y = icon.pos
    click(x, y)
    time.sleep(delay)


def press(key, delay = 0.5):
    pyautogui.press(key)
    time.sleep(delay)


def mouseOut():
    x, y = pyautogui.position()
    pyautogui.moveTo(800, y)


def mouseScroll(ticks=30):
    pyautogui.scroll(270, 790, ticks)


mouseScroll()