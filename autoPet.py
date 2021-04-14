import time
from threading import Thread

import skillAction
from heroes import heroLeveling
from tapping import tapClanmate, catchFairy, posionDagger, tapPetBurst
from ui.uiUtils import turnPlayScreen


def autoPetStart(evt):
    PetThread = Thread(target=autoPet, args=(1,))
    # not work SCThread.daemon = True
    PetThread.setDaemon(True)
    PetThread.start()
    # SCThread.join()


def onePetStart(evt):
    PetLoop()


def autoPet(arg):
    # global gAutoing

    while True:
        PetLoop()


def PetLoop():


    # check play screen status
    turnPlayScreen()

    # use skills
    skillAction.useAllSkillsButHS()

    # click clan mate
    tapClanmate()

    # pet burst 5s
    tapPetBurst(5)

    # posing dagger
    posionDagger()

    # heroes lv up
    heroLeveling()

    tapPetBurst(5)

    # catch fairy
    catchFairy()

    tapPetBurst(5)

    # wait next turn 10s
    time.sleep(1)