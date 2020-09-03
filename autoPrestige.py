import time

import autoit

from constants import Stucked_check_count, Stay_Same_Stage_count
from equipMenu import triggerHelmetChangeMode
from heroes import hero_btn_x
from uiUtils import bottomMenuExit, openBMenu, Icons

stageicon_checksum = 0
samestage_count = 0

def checkPrestige():

    global samestage_count, stageicon_checksum

    # check stuck in the same stage
    #   270, 60 , - 295, 75
    checksum = autoit.pixel_checksum(269, 53, 297, 82)
    print(f' check prestige prev cs {0}  cur cs {1} , ', {stageicon_checksum}, {checksum})

    if checksum == stageicon_checksum:
        samestage_count += 1
        print(f' Same  prestige prev cs {0}  cur cs {1} , count {2} ', {stageicon_checksum}, {checksum}, {samestage_count})

        # for HS build
        if samestage_count >= Stay_Same_Stage_count:
            triggerHelmetChangeMode(True)

        # not stucked ?
        if samestage_count < Stucked_check_count:
            return False
        else:
            pass
            # going to prestige
    else:
        # renew stage checksum
        stageicon_checksum = checksum
        samestage_count = 0
        return False

    resetRunVars()

    doPrestige()


    time.sleep(15)
    # time.sleep(1500)
    return True


def doPrestige():
    # click prestige btn
    bottomMenuExit()
    openBMenu(Icons.BMenu_Tap.name)
    #   click prestige btn , y 331
    autoit.mouse_click('left', hero_btn_x, 331, 1, 10)
    time.sleep(2)
    # # Prestige btn : 366, 890
    autoit.mouse_click('left', 366, 930, 1, 10)
    time.sleep(2)
    autoit.mouse_click('left', 442, 794, 1, 10)
    # wait

def resetRunVars():
    global samestage_count, stageicon_checksum
    # move through to prestige
    samestage_count = 0
    # reset vars
    stageicon_checksum = 0
    samestage_count = 0
    # reset other module
    triggerHelmetChangeMode(False)
