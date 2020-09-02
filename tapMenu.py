import time

import autoit

from constants import tapmenu_megaboost_btn_y, c_megaboost, tapmenu_btn_init_y, swordmaster_btn_y, \
    tapmenu_skill_lvbtn_x, CR_AtiveSkill_lvup_btn, CR_ActiveSkill_btn, CR_ActiveSkill_btn2
from heroes import hero_btn_x
from uiUtils import menuScrollUp, bottomMenuExit, openBMenu, Icons
from utils import IsColorAtCoord



def lvupActiveSkill():
    print(f'Tap menu lv up')

    # open bottom menu
    bottomMenuExit()
    openBMenu(Icons.BMenu_Tap.name)

    # scroll up
    menuScrollUp()

    # for lv up all skills
    # sword master lv up
    autoit.mouse_click('left', hero_btn_x, swordmaster_btn_y, 1, 5)
    time.sleep(0.5)
    # active skills
    # 451, 541, 626, 717, 802, 896  ,  x = 370  c= 0xe00000
    distance_btn_y = 88

    y = tapmenu_btn_init_y - distance_btn_y
    for i in range(6):
        y += distance_btn_y
        # check on skills  color ef6e14
        if not IsColorAtCoord(hero_btn_x, y, CR_ActiveSkill_btn) \
                and not IsColorAtCoord(hero_btn_x, y, CR_ActiveSkill_btn2):
            continue

        # color = autoit.pixel_get_color(hero_btn_x, y)
        # c = color & 0xff
        # print(f'tapmenu btn color', {y}, {hex(c)})
        # if 0xc6 <= c <= 0xcf:
        #     continue

        autoit.mouse_click('left', hero_btn_x, y, 1, 10)

        # check if possible lv up
        time.sleep(0.3)
        if IsColorAtCoord(tapmenu_skill_lvbtn_x, y, CR_AtiveSkill_lvup_btn):
            autoit.mouse_click('left', tapmenu_skill_lvbtn_x, y, 1, 5)
            time.sleep(0.1)

    # check Mega boost
    if not IsColorAtCoord(hero_btn_x, tapmenu_megaboost_btn_y, c_megaboost):
        autoit.mouse_click('left', hero_btn_x, tapmenu_megaboost_btn_y, 1, 10)

    bottomMenuExit()

