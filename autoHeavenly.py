import time
from threading import Thread

import constants
import skillAction
from autoPrestige import checkPrestige
from equipMenu import changeHelmet, getStuckedState
from heroes import heroLeveling
#from main import gAutoing
import main as m
from tapMenu import lvupActiveSkill
from tapping import tapPetMoney, tapClanmate, tapping, activateFS, catchFairy, posionDagger, tap, tapCursor, \
    posionDaggerAtOnce
from uiUtils import turnPlayScreen
from utils import IsColorInVRange, IsOneColorInVRange


def autoHSStart(evt):
    SCThread = Thread(target=autoHS, args=(1,))
    # not work SCThread.daemon = True
    SCThread.setDaemon(True)
    SCThread.start()
    #SCThread.join()


def oneHSStart(evt):
    m.activateWindow()
    HSLoop()

def autoHS(arg):
    #global gAutoing

    while m.getAutoing():
        HSLoop()


cur_action = 0
other_actions = ['fairy', 'heroes', 'fairy', 'heroes', 'helmet']
# other_actions = ['fairy', 'heroes', 'dagger','dagger', 'fairy', 'heroes', 'helmet']
hs_after_actions = ['heroes', 'heroes', 'fairy', 'heroes', 'heroes', 'fairy', 'heroes', 'helmet', 'fairy']
hs_hit_cnt = 0

cur_hsafter_action = 0

ManaEnoughHS_x = 100
ManaBar_y = 839

def enoughMana(mode):
    # check mana bar
    if mode == 'HS':
        # 112, 839
        x = ManaEnoughHS_x
        y = ManaBar_y
        if IsOneColorInVRange(x, y, one_color=0xff, yrange = 10, step = 2):
            # has enough mana
            print('HS : has!!  enough Mana ')
            return True
        else:
            print('HS : not enough Mana ')


    return False


def HSLoop():
    global cur_action, hs_hit_cnt, cur_hsafter_action
    constants.Stucked_check_count = 15

    # print(f' HSLoop, gauto ', {m.getAutoing()})
    # check play screen status
    turnPlayScreen()

    # use skills
    #   activate all skills,  but keep DS as 1 : it is not grant any damage increase
    skillAction.useAllSkillsButHS()

    # HS use
    #   only when mana is enough
    #if enoughMana():
    # used = skillAction.spamHS() if enoughMana('HS') else 0
    # check other essential skill is active
    used = False
    if skillAction.readySpam():
        used = skillAction.spamHS()

    if enoughMana('HS'):
        mode = 'spamming'
    else:
        mode = 'otheraction'

    print(f'HS loop: used 1, cur_act 2, hs hit cnt 3, cur_hsafter_action  4', {used}, {cur_action}, {hs_hit_cnt}, {cur_hsafter_action})

    # wait for next HS
    if 'spamming' == mode:
        posionDaggerAtOnce()
        # click pet
        tapClanmate()
        tapPetMoney()

        hs_hit_cnt += 1

        # mix other actions while spamming
        if hs_hit_cnt > 8:
            hs_hit_cnt = 0
            hsafter_action = hs_after_actions[cur_hsafter_action]
            doOtherAction(hsafter_action)
            cur_hsafter_action = 0 if cur_hsafter_action >= len(hs_after_actions) - 1 else cur_hsafter_action + 1
        else:
            # tap 1 sec
            tap(325, 780)
            for i in range(10):
                tapCursor()

            time.sleep(1.1)
    else:   # not enough mana -> do other action to wait fill mana

        # not used . do other action one at a time
        other_action = other_actions[cur_action]

        doOtherAction(other_action)
        cur_action = 0 if cur_action >= len(other_actions)-1 else cur_action + 1
        hs_hit_cnt = 0  # clear to restart spamming
        time.sleep(2)  # wait a little until refill mana


    # check prestige & restart active skills
    if checkPrestige():
        lvupActiveSkill()

    # move cursor to indicate loop action is over
    tap(325, 780)




def doOtherAction(other_action):
    print(f' HS : do others ', {other_action})
    if other_action == 'fairy':
        # catch fairy
        catchFairy('short') # short version
    elif other_action == 'heroes':
        tapPetMoney()   # get money before heroes lv up
        # heroes lv up
        heroLeveling()
    elif other_action == 'dagger':
        # posing dagger
        #   only do when stucked more than once at the same stage
        #if getStuckedState():
        posionDaggerAtOnce()
    elif other_action == 'helmet':
        # set hero type equip
        changeHelmet()
    else:
        pass
