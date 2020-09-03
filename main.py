# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time

import autoit
from system_hotkey import SystemHotkey

from autoHeavenly import *
from autoPet import autoPetStart, onePetStart
from autoPrestige import checkPrestige, doPrestige
from equipMenu import changeHelmet, triggerHelmetChangeMode, getStuckedState
from heroes import checkNewlyActivatedHero
from skillAction import *
from autoSC import *
from tapMenu import lvupActiveSkill
from tapping import tapping, tapCursor

Client = "LDPlayer"
ClientClass = "[CLASS:LDPlayerMainFrame]"


def register_hotkey():
    '''
    hk = SystemHotkeys()
    hk.register(('control', 'shift', 'h'), callback=lambda: print("Easy!"))
    hk.unregister(('control', 'shift', 'h'))
    '''

    hk.register(('control', 'shift', 's'), callback=autoSCStart)
    hk.register(('control', 'shift', 'z'), callback=oneSCStart)
    hk.register(('control', 'shift', 'x'), callback=autoHSStart)
    hk.register(('control', 'shift', 'c'), callback=oneHSStart)
    hk.register(('f4', 'f4', 'f4'), callback=testFunction)
    hk.register(('f3', 'f3', 'f3'), callback=useSkills)
    hk.register(('f8', 'f8', 'f8'), callback=goTapping)
    hk.register(('control', 'shift', 'a'), callback=stopAutoing)
    hk.register(('control', 'shift', 'e'), callback=exitFunction)
    # hk.register(('control', 'shift', 'h'), callback=testFunction )


hk = SystemHotkey()

gAutoing = True

testbool = True
def testFunction(evt):

    print('test')
    # constants.ManaEnoughHS_x = 150
    # ret = checkNewlyActivatedHero()
    # print(f'ret ', {ret})

    heroLeveling()
    # doPrestige()
    # time.sleep(15)
    # lvupActiveSkill('SC')
    # triggerHelmetChangeMode(True)
    # changeHelmet()
    # from timeit import default_timer as timer
    #
    # start = timer()
    # # ...
    # time.sleep(0.7)
    # end = timer()
    # print(end - start)

    # ret  = enoughMana('HS')
    # print(f'ret ', {ret})
    # getStuckedState()
    # triggerHelmetChangeMode(True)
    # getStuckedState()

    # global  testbool
    #
    # testbool = not testbool
    # triggerHelmetChangeMode(testbool)
    # changeHelmet()

    # if checkPrestige():
    #     lvupActiveSkill()
    #
    # # set hero type equip
    # changeHelmet()


    # lvupActiveSkill()
    # bottomMenuExit()
    # useAllSkills()
    # BottomMenuExit()


def init_env():
    # Set coordinate config
    autoit.opt("MouseCoordMode", 0)
    autoit.opt("PixelCoordMode", 0)

    # autoit.hot_key_set("{ESC}", "OnExit")
    # autoit.hot_key_set("{F4}", "testFunction")

    activateWindow()

    global gAutoing
    gAutoing = True


def activateWindow():
    # window align
    autoit.win_activate(ClientClass)
    autoit.win_move(Client, 0, 0)


def getAutoing():
    global gAutoing
    print(f'get auto ', {gAutoing})
    return gAutoing

def stopAutoing(evt):
    global gAutoing
    print(f'Try Stop Auto Thread')
    gAutoing = not gAutoing
    print(f'toglle auto  ', {gAutoing})


def exitFunction(evt):
    print('exit')

    global gAutoing
    print(f' exit, gauto ', {gAutoing})

    exit(0)
    try:
        hk.unregister(('control', 'shift', 'a'))
        hk.unregister(('control', 'shift', 's'))
        hk.unregister(('control', 'shift', 'e'))
    except:
        pass

    exit(0)


def useSkills(evt):
    useAllSkills()




# infinite loop Falut!!!
def goTapping(evt):
    # while True:
    tapCursor()


def BottomMenuExit():
    menu_exit_x = 522
    menu_exit_y = 595
    autoit.mouse_click("left", menu_exit_x, menu_exit_y, 1, 5)


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
    BottomMenuExit()

    while 1:
        time.sleep(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
