import enum
import time

import autoit

import heroes
from constants import CR_HeroEleTypes, Icons, HeroEleType
from uiUtils import bottomMenuExit, openBMenu
from utils import IsColorInRect, IsColorAtCoord

_b_changing = False

def getStuckedState():
    print(f' getStuckedState ', {_b_changing})
    return _b_changing

def triggerHelmetChangeMode(on):
    global  _b_changing
    print(f' helm change mode ' , {on})
    _b_changing = on
    print(f' helm change mode after set' , {_b_changing})

def changeHelmet():

    global _b_changing
    if _b_changing == False:
        return

    # get highest hero type
    # coord 368,281 +- 4, 6
        # Spell:  CR 0x00b1CA
        # melee: CR 0xfb8649
        # Range: 0x6bBD42
    htype = heroes.hero_type
    print(f' change helmet get he type ', {htype})

    # move to helmet equip tap
    openBMenu(Icons.BMenu_Equip.name)
    # select helm tap
    autoit.mouse_click('left', 136, 135, 1, 10)

    # find proper type of a helmet
    # spell  497,229
    # range  x, 783
    # melee  x, 598
    # 1st row :  159,250 - 193, 260
    # x, 341,  - x2, 351
    # 3rd :  x, 432, - x2, 442
    # 4th : 524 - 534
    # 5 : 617 - 625
    # 6 : 707 - 717
    #7:  799 - 807
    # y step 91  interval : 10
    for y in range(248, 797, 91):
        helm_type_checksum = autoit.pixel_checksum(159, y, 193, y+10)
        print(f'helm checksum y: ', {y}, {hex(helm_type_checksum)})

    helm_type_checksum =  autoit.pixel_checksum(159, 250, 193, 260)
    print(f'helm checksum 1: ', {hex(helm_type_checksum)})
    helm_type_checksum =  autoit.pixel_checksum(159, 341, 193, 351)
    print(f'helm checksum 1: ', {hex(helm_type_checksum)})
    helm_type_checksum =  autoit.pixel_checksum(159, 432, 193, 442)
    print(f'helm checksum 1: ', {hex(helm_type_checksum)})
    helm_type_checksum =  autoit.pixel_checksum(159, 524, 193, 534)
    print(f'helm checksum 1: ', {hex(helm_type_checksum)})

    helm_type_checksum =  autoit.pixel_checksum(159, 617, 193, 625)
    print(f'helm checksum 1: ', {hex(helm_type_checksum)})
    helm_type_checksum =  autoit.pixel_checksum(159, 707, 193, 717)
    print(f'helm checksum 1: ', {hex(helm_type_checksum)})
    helm_type_checksum =  autoit.pixel_checksum(159, 799, 193, 807)
    print(f'helm checksum 7: ', {hex(helm_type_checksum)})

    init_y = 232
    interval = 91
    equip_spell_y = 0
    equip_range_y = 4
    equip_melee_y = 2

    equip_x = 500

    if htype == HeroEleType.Melee:
        y = equip_melee_y
    elif htype == HeroEleType.Range:
        y = equip_range_y
    elif htype == HeroEleType.Spell:
        y = equip_spell_y
    else:
        y = -2 # exit btn y offset

    # check already equipped
    equip_y = init_y + y * interval
    if not IsColorAtCoord(equip_x, equip_y, 0x59ac3d):
        bottomMenuExit()
        return

    # equip
    autoit.mouse_click('left', equip_x, equip_y, 1, 10)

    bottomMenuExit()
    time.sleep(1)

    # clear trigger flag
    _b_changing = False


