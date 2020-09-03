import time
from threading import Thread

import constants
import skillAction
from autoPrestige import checkPrestige, resetRunVars, doPrestige
from equipMenu import changeHelmet, getStuckedState
from heroes import heroLeveling
#from main import gAutoing
import main as m
from tapMenu import lvupActiveSkill
from tapping import tapPetMoney, tapClanmate, tapping, activateFS, catchFairy, posionDagger, tap, tapCursor, \
    posionDaggerAtOnce
from uiUtils import turnPlayScreen
from utils import IsColorInVRange, IsOneColorInVRange
from timeit import default_timer as timer


restart = True
start_time = 0

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
    global restart

    while m.getAutoing():
        restart = False # started
        HSLoop()
        fastPrestigeTimeCheck()

cur_action = 0
other_actions = ['fairy', 'heroes', 'fairy', 'heroes', 'helmet']
# other_actions = ['fairy', 'heroes', 'dagger','dagger', 'fairy', 'heroes', 'helmet']
hs_after_actions = ['hero_helmet', 'heroes', 'heroes']
hs_hit_cnt = 0

cur_hsafter_action = 0



def enoughMana(mode):
    # check mana bar
    if mode == 'HS':
        # 112, 839
        x = constants.ManaEnoughHS_x
        y = constants.ManaBar_y
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


    if enoughMana('HS'):
        mode = 'spamming'
        if skillAction.readySpam():
            used = skillAction.spamHS()

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
        if hs_hit_cnt > constants.HS_Spamming_Keep_cnt:
            hs_hit_cnt = 0
            hsafter_action = hs_after_actions[cur_hsafter_action]
            doOtherAction(hsafter_action)
            cur_hsafter_action = 0 if cur_hsafter_action >= len(hs_after_actions) - 1 else cur_hsafter_action + 1
        else:
            # catch fairy on moving area tap 1 sec
            tap(487, 299)
            for i in range(8):
                tapCursor()

            time.sleep(0.9)
    else:   # not enough mana -> do other action to wait fill mana

        # not used . do other action one at a time
        pass

        # check prestige & restart active skills
        """
        other_action = other_actions[cur_action]

        doOtherAction(other_action)
        cur_action = 0 if cur_action >= len(other_actions)-1 else cur_action + 1
        hs_hit_cnt = 0  # clear to restart spamming
        time.sleep()  # wait a little until refill mana
        
        """

        # time.sleep(3)  # wait a little until refill mana
        # catch fairy on moving area tap 1 sec
        catchFairy()
        # time.sleep(0.9)

    if checkPrestige():
        global restart
        lvupActiveSkill('HS')
        restart = True

    # move cursor to indicate loop action is over
    tap(325, 780)




def doOtherAction(other_action):
    print(f' HS : do others ', {other_action})
    if other_action == 'fairy':
        # catch fairy
        # catchFairy('short') # short version
        pass
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
        #  move into hero leveling ()
        # changeHelmet()
        pass
    elif other_action == 'hero_helmet':
        heroLeveling()
        # move into hero leveling  changeHelmet()
    else:
        pass


def fastPrestigeTimeCheck():
    from timeit import default_timer as timer

    global start_time
    if restart:
        start_time = timer()
    # ...
    # time.sleep(0.7)
    end = timer()

    elapsed = end - start_time
    print(f'time check ' , {elapsed})

    # if elapsed > 5*60:
    #     resetRunVars()
    #     doPrestige()
    #     time.sleep(15)
    #     global restart
    #     lvupActiveSkill('HS')
    #     restart = True