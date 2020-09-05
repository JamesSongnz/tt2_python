import enum
import time

import autoit

from constants import CR_HeroEleTypes, Icons, HeroEleType, Equip_Ele_Spell_y, Equip_Ele_Range_y, Equip_Ele_Melee_y, \
    SlashType
from uiUtils import bottomMenuExit, openBMenu
from utils import IsColorInRect, IsColorAtCoord, IsColorInVRange, findColorInVRange

_b_changing = False

# eqip icon w, h  : 63 x 63
# checksum box 48x48 :
# margin start : 15x 15
Equip_Icon_x = 14  # 14
Equip_Icon_Check_padding = 15
Equip_Icon_Check_In_w = 33
Equip_Icon_Check_Rect_w = 48
Equip_Icon_w = 63

# find Icon Position
Equip_Icon_Start_y = 198
Equip_Icon_Gap = 91




def getStuckedState():
    print(f' getStuckedState ', {_b_changing})
    return _b_changing

def triggerHelmetChangeMode(on):
    global  _b_changing
    print(f' helm change mode ' , {on})
    _b_changing = on
    print(f' helm change mode after set' , {_b_changing})

def changeHelmet(mode='stucked', hero_type=HeroEleType.Error):

    global _b_changing
    if 'stucked' == mode and _b_changing == False:
        return

    # get highest hero type
    # coord 368,281 +- 4, 6
        # Spell:  CR 0x00b1CA
        # melee: CR 0xfb8649
        # Range: 0x6bBD42
    print(f' change helmet get he type ', {hero_type})

    # # move to helmet equip tap
    openBMenu(Icons.BMenu_Equip.name)

    # select helm tap
    if 0x424044 != autoit.pixel_get_color(126, 166):
        autoit.mouse_click('left', 136, 135, 1, 3)
        time.sleep(0.3)

    # row = getRowOfEquipment(tap='helm', kind=hero_type)
    row = getRowOfEquipmentPattern(tap='helm', kind=hero_type)
    print(f' Found Hero type at row ', {hero_type}, {row})

    # equip cur type equipment
    if row < 0:
        # not found
        return False

    # # y step 91  interval : 10
    # y = 0

    # #test
    # helm_type_checksum = autoit.pixel_checksum(14, 381, 14+63, 381 + 63)
    # print(f'helm checksum y3: ', {y}, {hex(helm_type_checksum)})
    #
    # helm_type_checksum = autoit.pixel_checksum(14, 564, 14+63, 564 + 63)
    # print(f'helm checksum 5: ', {y}, {hex(helm_type_checksum)})
    #
    # helm_type_checksum = autoit.pixel_checksum(14, 655, 14+63, 655 + 63)
    # print(f'helm checksum 666: ', {y}, {hex(helm_type_checksum)})
    #
    # helm_type_checksum = autoit.pixel_checksum(14, 746, 14+63, 746 + 63)
    # print(f'helm checksum 777: ', {y}, {hex(helm_type_checksum)})

    # for y in range(Equip_Icon_y, 857, 91):
    #     helm_type_checksum = autoit.pixel_checksum(Equip_Icon_x, y, Equip_Icon_x2, y+Equip_Icon_h)
    #     print(f'helm checksum y: ', {y}, {hex(helm_type_checksum)})
    #     time.sleep(0.5)
    #     autoit.mouse_move(Equip_Icon_x, y)
    #     helm_type_checksum = 0


    # find specific colors for the item
    #  Helm of Tears 0x005b7d ,

    #
    # if hero_type == HeroEleType.Melee:
    #     row = Equip_Ele_Melee_y
    # elif hero_type == HeroEleType.Range:
    #     row = Equip_Ele_Range_y
    # elif hero_type == HeroEleType.Spell:
    #     row = Equip_Ele_Spell_y
    # else:
    #     row = -2 # exit btn y offset


    equiping(row)

    bottomMenuExit()
    time.sleep(1)

    # clear trigger flag
    _b_changing = False

    return True


def changeSlash(type=SlashType.SCPorter):

    print(f' change changeSlash get he type ', {type})

    # # move to helmet equip tap
    openBMenu(Icons.BMenu_Equip.name)
    # select slash tap
    if 0x424044 != autoit.pixel_get_color(355, 166):
        autoit.mouse_click('left', 355, 135, 1, 3)
        time.sleep(0.3)

    row = getRowOfEquipmentPattern(tap='slash', kind=type)
    print(f' Found slash type at row ', {type}, {row})

    # equip cur type equipment
    if row < 0:
        # not found
        return False

    equiping(row)

    bottomMenuExit()
    return True


def equiping(row):
    # check already equipped
    equip_y = Equip_Icon_Start_y + row * Equip_Icon_Gap + 30 # btn offset
    equip_btn_x = 463
    if not IsColorAtCoord(equip_btn_x, equip_y, check_color=0x58aa3d):
        bottomMenuExit()
        return

    # equip
    autoit.mouse_click('left', equip_btn_x, equip_y, 1, 10)


Equip_Lists  = \
{
    # type: offsetx, offsety, pixels[2x2], 'name'
    # type: checksum , 'name'
    'helm': [
            [HeroEleType.Spell, 0xd12ffda, 'helm of tears'],
            [HeroEleType.Range, 0x721e51ac, 'Fedora'],
            [HeroEleType.Melee, 0x784c6ee0, 'Team Cap'],
            ],
}

# Warining: does not work.. check sum is always changing when wheel scroll.
def helmFindChecksumTest():
    print(f' Checksum ')
    x = Equip_Icon_x+ Equip_Icon_Check_padding
    y = 290 + Equip_Icon_Check_padding #290
    x2 = Equip_Icon_x + Equip_Icon_Check_Rect_w
    y2= 290 + Equip_Icon_Check_Rect_w


    c = -0x48bac863
    print(f' Defie ', {x}, {y}, {hex(c)})

    autoC = autoit.pixel_checksum(x, y, x2, y2)
    print(f' auto.it ', {x}, {y}, {x2}, {y2}, {hex(autoC)})

    # found = IsColorInRect(x, y, pixels[i], xrange=1, yrange=1, step=1)
    icon_checksum = getIconChecksum(y-5)
    print(f'found pixel x y  icon check ', {c==icon_checksum}, {x}, {y}, {hex(icon_checksum)})


# arg : tap, kind of equip tap
# ret : row of wanted type equip
def getRowOfEquipment(tap='helm', kind=-1):
        # get equip lists

    equips = Equip_Lists[tap]

    for i, y in enumerate(range(Equip_Icon_Start_y, Equip_Icon_Gap * 8, Equip_Icon_Gap)):

        icon_checksum = getIconChecksum(y)

        # identify this item
        type = getTypeOfEquipment(equips, icon_checksum)

        if type == kind:
            return i # return row index

    return -1

def getIconChecksum(y):
    # find actuall icon start y
    # finid block pixel
    adjusted_y = findColorInVRange(Equip_Icon_x, y, color=0x000000, yrange=10, step=1, offset=0x0)
    print(f' adjusted_y ' , {adjusted_y})
    # fail to find Icon region
    if -1 == adjusted_y:
        return 0x000000

    # found Icon start y
    icon_y = y + adjusted_y

        # compare checksum at icon rect
    icon_checksum = autoit.pixel_checksum(Equip_Icon_x + Equip_Icon_Check_padding,
                                          icon_y + Equip_Icon_Check_padding,
                                          Equip_Icon_x + Equip_Icon_Check_Rect_w,
                                          icon_y + Equip_Icon_Check_Rect_w)
    # icon_checksum = autoit.pixel_checksum(Equip_Icon_x + 5,
    #                                       icon_y + 20,
    #                                       Equip_Icon_x + 10,
    #                                       icon_y + 30)
    print(f' Icon cs ', {icon_y}, {hex(icon_checksum)})
    return icon_checksum

def getTypeOfEquipment(equips, checksum):
    for e in equips:
        if e[1] == checksum:
            return e[0]


################################# pattern match way

Equip_patten_Lists  = \
{
    # type: offsetx, offsety, pixels[1], 'name'
    'helm': [
        # 32, 303 - 008BA3  ( 14, 290 )
            [HeroEleType.Spell, 18, 13, (0x008BA3,), 'helm of tears'],
            [HeroEleType.Range, 21, 19, (0xF9B30D,), 'Fedora'],
            # [HeroEleType.Melee, 13, 24, (0xE5E5E5,), 'Valkyrie Circlet'],
            [HeroEleType.Melee, 30, 12, (0xDB6700,), 'Dusty'],
            ],
    'slash': [
            [SlashType.SCPorter, 22, 28, (0x1C559A, 0x1E75BA,), 'Mythtical Echo'],
            [SlashType.SCPush, 21, 15, (0x267BF7, 0x1E72EE,), 'Lapis Lazuli']
            ],
}


def helmFindPatterntest():

    # 32, 303 - 008BA3
    x = 32
    y =     303
    c = 0x008ba3
    print(f' Defie ', {x}, {y}, {hex(c)})

    autoP = autoit.pixel_get_color(x, y)
    print(f' auto.it ', {x}, {y}, {hex(autoP)})

    # found = IsColorInRect(x, y, pixels[i], xrange=1, yrange=1, step=1)
    found = IsColorAtCoord(x, y, c, offset=0x0)
    print(f'found pixel x y on p, equip p ', {found}, {x}, {y})


# arg : tap, kind of equip tap
# ret : row of wanted type equip
def getRowOfEquipmentPattern(tap='helm', kind=HeroEleType.Error):
    # get equip lists

    equips = Equip_patten_Lists[tap]

    for i, y in enumerate(range(Equip_Icon_Start_y, Equip_Icon_Start_y+20+Equip_Icon_Gap * 8, Equip_Icon_Gap)):

        icon_start_y = getIconYstart(y)
        print(f' got icon start y ', {icon_start_y})
        if icon_start_y == -1: # error
            continue

        for equip in equips:
            xoffset = equip[1]
            yoffset = equip[2]
            pixels = equip[3]

            # equip pattern found at y
            print(f'try search equip pattern ', {xoffset}, {yoffset}, {hex(pixels[0])}, {equip[4]})
            type = equip[0] if comparePatternOnScr(Equip_Icon_x+xoffset, icon_start_y+yoffset, pixels) else -1
            print(f' found type kind ', {type}, {kind})

            if type == kind:
                return i # return row index

    return -1



def getIconYstart(y):

    yoffset = findColorInVRange(Equip_Icon_x+2, y, color=0x000000, yrange=10, step=1, offset=0x0)

    # fail to find Icon region
    if -1 == yoffset:
        return -1

    # found Icon start y
    icon_y = y + yoffset

    return icon_y

# pixels on the same y
def comparePatternOnScr(x, y, pixels):
    for i, pixel in enumerate(pixels):

        # try region
        # found = IsColorInRect(x, y, pixels[i], xrange=1, yrange=1, step=1)
        found = IsColorAtCoord(x+i, y, pixels[i], offset=0xf)
        print(f'found pixel x y on p, equip p ', {found}, {x+i}, {y}, {hex(pixels[i])})
        if not found:
            return False

        # not work
        # p = autoit.pixel_get_color(x+i, y)
        # print(f'compare pixels x y on p, equip p ', {x}, {y}, {hex(p)}, {hex(pixels[i])})
        # if pixels[i] != p:
        #     return False
    return True



