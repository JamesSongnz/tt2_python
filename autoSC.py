import time
from threading import Thread

import skillAction
from heroes import heroLeveling
#from main import gAutoing
import main as m
from tapping import tapPetMoney, tapClanmate, tapping, activateFS, catchFairy, posionDagger
from uiUtils import turnPlayScreen

''' 
class Auto:
    ing = False
    
class AutoSC(Auto):

'''


def autoSCStart(evt):
    SCThread = Thread(target=autoSC, args=(1,))
    # not work SCThread.daemon = True
    SCThread.setDaemon(True)
    SCThread.start()
    #SCThread.join()


def oneSCStart(evt):
    SCLoop()

def autoSC(arg):
    #global gAutoing

    while m.getAutoing():
        SCLoop()


def SCLoop():
    print(f' autoSC, gauto ', {m.getAutoing()})
    # check play screen status
    turnPlayScreen()
    # use skills
    skillAction.useAllSkillsButHS()
    # click pet
    # use dagger instead of tapPetMoney()
    tapClanmate()
    # active FS
    #activateFS()
    # posing dagger
    posionDagger()
    # heroes lv up
    heroLeveling()
    # catch fairy
    catchFairy()
    # wait next turn 10s
    time.sleep(5)