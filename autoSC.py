import time
from threading import Thread

import skillAction
from autoPrestige import checkPrestige
from equipMenu import changeHelmet
from heroes import heroLeveling
#from main import gAutoing
import main as m
from tapMenu import lvupActiveSkill
from tapping import tapPetMoney, tapClanmate, tapping, activateFS, catchFairy, posionDagger, tap
from uiUtils import turnPlayScreen

''' 
class Auto:
    ing = False
    
class AutoSC(Auto):

'''

SCRunMode = 'push'

def autoSCStart(evt):
    SCThread = Thread(target=autoSC, args=(1,))
    # not work SCThread.daemon = True
    SCThread.setDaemon(True)
    SCThread.start()
    #SCThread.join()


def oneSCStart(evt):
    m.activateWindow()
    SCLoop()

def autoSC(arg):
    #global gAutoing

    while m.getAutoing():
        SCLoop()


def SCLoop():
    global SCRunMode
    print(f' autoSC, gauto ', {m.getAutoing()})
    # check play screen status
    turnPlayScreen()
    # use skills
    skillAction.useAllSkillsButHS()
    # click pet
    # use dagger instead of tapPetMoney()
    tapClanmate()

    if SCRunMode == 'push':
        # posing dagger
        posionDagger()
    else:
        tapPetMoney()
        # active FS
        activateFS()

    # catch fairy
    catchFairy()

    # heroes lv up
    heroLeveling()

    # check prestige & restart active skills
    if checkPrestige():
        lvupActiveSkill()

    # set hero type equip
    changeHelmet()

    # move cursor to indicate loop action is over
    tap(325, 780)

    # wait next turn 10s
    time.sleep(5)