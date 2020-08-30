from threading import Thread

import skillAction
from heroes import heroLeveling
#from main import gAutoing
import main as m
from tapping import tapPetMoney, tapClanmate, tapping

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


def autoSC(arg):
    #global gAutoing

    while m.getAutoing():
        print(f' autoSC, gauto ', {m.getAutoing()})
        # use skills
        skillAction.useAllSkillsButHS()

        '''
        # click pet
        tapPetMoney()
        tapClanmate()

        # active FS
        tapping()

        # heroes lv up
        heroLeveling()

        # catch fairy
        '''