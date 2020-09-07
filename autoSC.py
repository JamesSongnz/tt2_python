import time
from threading import Thread

import skillAction
from autoPrestige import checkPrestige
from constants import SlashType, Icons
from equipMenu import changeHelmet, changeSlash
from heroes import heroLeveling
#from main import gAutoing
import main as m
from tapMenu import lvupActiveSkill, cancelSkills
from tapping import tapPetMoney, tapClanmate, tapping, activateFS, catchFairy, posionDagger, tap, simpleClickFairy, \
    isAnyDagger, tapFairyCollect
from uiUtils import turnPlayScreen, checkSlowDown, menuScrollUpLong, bottomMenuExit, openBMenu, turnOnBossBattle, \
    menuScrollUp

''' 

72926
1.09 108

'''

SCRunMode = 'push'
# SCRunMode = 'farm'

def autoSCStart(evt):
    SCThread = Thread(target=autoSC, args=(1,))
    # not work SCThread.daemon = True
    SCThread.setDaemon(True)
    SCThread.start()
    #SCThread.join()


def oneSCStart(evt):
    m.activateWindow()
    SCLoop()


FirstTimeRun = True
auto_start_timer = 0
Paused_Auto_Interval = 220
# allow to do other actions while auto ing...
def rareSCStart(evt):
    from timeit import default_timer as timer
    global auto_start_timer, FirstTimeRun

    SCLoop()

    # if FirstTimeRun:
    auto_start_timer = timer()
        # FirstTimeRun = False

    while m.getAutoing():

        # time.sleep(3)
        time.sleep(30)
        end = timer()
        elapsed = end - auto_start_timer
        print(f' time : ', {elapsed})

        if elapsed > Paused_Auto_Interval:
            m.activateWindow()

            # engage Boss Battle
            turnOnBossBattle()

            cancelSkills()

            # open bottom menu
            bottomMenuExit()
            openBMenu(Icons.BMenu_Heroes.name)

            # menuScrollUp()
            #do heroes lv up at the first time
            heroLeveling()

            # do SC actions excute
            SCLoop()

            #reset timer
            auto_start_timer = timer()


def autoSC(arg):
    #global gAutoing

    # check newly start
    if skillAction.emptySkillCircle():
        lvupActiveSkill('SC')

    # equip slash for SC Porter at first
    # changeSlash(SlashType.SCPorter)

    while m.getAutoing():
        SCLoop()


nothing_done_loop_cnt = 0

def SCLoop():
    global SCRunMode, nothing_done_loop_cnt


    print(f' autoSC, gauto ', {m.getAutoing()})
    # check play screen status
    turnPlayScreen()
    # use skills
    skillAction.useAllSkillsButHS()
    # click pet
    # use dagger instead of tapPetMoney()
    tapClanmate()

    if SCRunMode == 'push':

        # try 3 times to use all daggers
        while isAnyDagger():
            nothing_done_loop_cnt = True
            # posing dagger
            posionDagger()
            # check skill is activated.
            skillAction.useAllSkillsButHS()

            nothing_done_loop_cnt = 1 # to skip fiary & leveliing


    else:
        tapPetMoney()
        # active FS
        activateFS()

    # catch fairy
    # catch only nothing has done before
    # if (nothing_done_loop_cnt % 5) == 0:
        # catchFairy()
    simpleClickFairy()
    time.sleep(1)

    tapFairyCollect()

    # do per 5 loop times.
    if (nothing_done_loop_cnt % 5) == 0:
        # heroes lv up
        tapPetMoney()
        heroLeveling()
    #  move into hero leveling () set hero type equip
    # changeHelmet()

    # check prestige & restart active skills
    if checkPrestige():
        lvupActiveSkill()

    # check slow down
    # if 1:
    # if checkSlowDown():
    if False:
        changeSlash(SlashType.SCPush)

    # move cursor to indicate loop action is over
    tap(325, 780)

    # wait next turn 10s
    time.sleep(1.5)
    nothing_done_loop_cnt += 1