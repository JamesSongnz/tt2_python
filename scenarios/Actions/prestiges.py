import time

import autoit

from data.constants import Stucked_check_count, Stay_Same_Stage_count, Icons
from data.coordinates import Icons_coord
from equipMenu import triggerHelmetChangeMode
from heroes import hero_btn_x
from scenarios.Actions.action import Action
from ui import uiAction
from ui.menus import bottomMenuExit, openBtMenu

PrestigeBtn_y = 331

stageicon_checksum = 0
samestage_count = 0


class Prestige(Action):

    def do(self):
        self.doPrestige()

    def checkPrestige(self):

        global samestage_count, stageicon_checksum

        # check stuck in the same stage
        #   270, 60 , - 295, 75
        checksum = autoit.pixel_checksum(269, 53, 297, 82)
        print(f' check prestige prev cs {0}  cur cs {1} , ', {stageicon_checksum}, {checksum})

        if checksum == stageicon_checksum:
            samestage_count += 1
            print(f' Same  prestige prev cs {0}  cur cs {1} , count {2} ', {stageicon_checksum}, {checksum}, {samestage_count})

            # # for HS build
            # if samestage_count >= Stay_Same_Stage_count:
            #     triggerHelmetChangeMode(True)

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

        self.resetRunVars()

        self.doPrestige()


        time.sleep(15)
        # time.sleep(1500)
        return True


    def doPrestige(self):
        """ click prestige btn      """

        bottomMenuExit()
        openBtMenu(Icons_coord.BMenu_Tap)

        #   click prestige btn , y 331
        uiAction.clickIcon(Icons_coord.Prestige_Panel_Btn)
        time.sleep(2)

        uiAction.clickIcon(Icons_coord.Prestige_Window_Btn)
        time.sleep(1)

        uiAction.clickIcon(Icons_coord.Prestige_Confirm_Btn)

        # # wait
        time.sleep(10)
        

    def resetRunVars(self):
        global samestage_count, stageicon_checksum
        # move through to prestige
        samestage_count = 0
        # reset vars
        stageicon_checksum = 0
        samestage_count = 0
        # reset other module
        # triggerHelmetChangeMode(False)



    def fastPrestigeTimeCheck(self):
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