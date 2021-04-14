# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import autoit

from hotkey import register_hotkey
from ui.window import activateWindow


gAutoing = True



def init_env():
    # Set coordinate config
    autoit.opt("MouseCoordMode", 1)
    autoit.opt("PixelCoordMode", 1)

    # autoit.hot_key_set("{ESC}", "OnExit")
    # autoit.hot_key_set("{F4}", "testFunction")

    activateWindow()

    global gAutoing
    gAutoing = True



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # auto it test

    '''
    autoit.run("notepad.exe")
    autoit.win_wait_active("[CLASS:Notepad]", 3)
    autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
    autoit.win_close("[CLASS:Notepad]")
    autoit.control_click("[Class:#32770]", "Button2")
    '''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # set autoit env
    init_env()
    register_hotkey()

    print_hi('PyCharm - click ')

    # mouse click test
    # BottomMenuExit()

    while 1:
        time.sleep(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
