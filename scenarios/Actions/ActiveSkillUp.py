import enum
import time

import data
from data import utils, constants
from data.constants import tapmenu_skill_lvbtn_x, CR_AtiveSkill_lvup_btn, CR_ActiveSkill_btn, CR_ActiveSkill_btn2, \
    hero_btn_x
from data.coordinates import Icons_coord
from data.utils import ratioConvert
from scenarios.Actions.action import Action
from ui import menus, uiAction
from ui.menus import bottomMenuExit
from utils import IsColorAtCoord


class ActiveSkillUp(Action):
    # max = -1 , 0 : disable, 1~ : lv 1
    tap_active_skill_lists = {
        'SC': [('HS', -1), ('DS', -1), ('HM', -1), ('FS', -1), ('WC', -1), ('SC', -1)],
        'HS': [('HS', -1), ('DS', 1), ('HM', -1), ('FS', -1), ('WC', -1), ('SC', -1)],
        'PET': [('HS', -1), ('DS', 1), ('HM', -1), ('FS', 1), ('WC', -1), ('SC', -1)],
    }

    class Skills_coord(enum.Enum):
        # Tap panel
        Tap_Sword_lv_Btn = (482, 215, 'Sword')

        Skill_HS_Btn = (482, 462, 'HS')
        Skill_DS_Btn = (482, 550, 'DS')
        Skill_HM_Btn = (482, 645, 'HM')
        Skill_FS_Btn = (482, 736, 'FS')
        Skill_WC_Btn = (482, 825, 'WC')
        Skill_SC_Btn = (482, 915, 'SC')

        def __init__(self, x, y, string, sk=None):
            self.ratio = 1.25
            self.point = (x, y)
            self.str = string
            self.sk = sk

        def scaleup(self):
            return data.utils.ratioConvertTuple(self.point, self.ratio)

        @property
        def pos(self):
            if constants.SCREEN_SCALE_RATIO != 1:
                return self.scaleup()
            else:
                return self.point


    def do(self):
        self.doSkillUp()

    def doSkillUp(self):
        print(f'Tap menu lv up')

        # open bottom menu
        bottomMenuExit()
        menus.openBtMenu(Icons_coord.BMenu_Tap)

        # scroll up
        uiAction.mouseScroll()

        # for lv up all skills
        # sword master lv up
        uiAction.clickMultiple(Icons_coord.Tap_Sword_lv_Btn)

        time.sleep(0.5)
        # active skills
        # 451, 541, 626, 717, 802, 896  ,  x = 370  c= 0xe00000
        distance_btn_y = 88

        mode = 'PET'
        skill_list = ActiveSkillUp.tap_active_skill_lists[mode]

        for s in self.Skills_coord:
            on = [on for sk, on in skill_list if sk == s.str]
            print(on)
            if on and on[0] >= 1:

                # check on skills  color ef6e14
                skill_btn_right_x = ratioConvert(548)
                if not IsColorAtCoord(skill_btn_right_x, s.pos[1], CR_ActiveSkill_btn) \
                        and not IsColorAtCoord(skill_btn_right_x, s.pos[1], CR_ActiveSkill_btn2):
                    continue

                # color = autoit.pixel_get_color(hero_btn_x, y)
                # c = color & 0xff
                # print(f'tapmenu btn color', {y}, {hex(c)})
                # if 0xc6 <= c <= 0xcf:
                #     continue

                # autoit.mouse_click('left', hero_btn_x, y, 1, 10)
                uiAction.clickIcon(s)


                # check lv number
                if on[0] == 1:
                    continue

                # else lv up max
                # check if possible lv up
                time.sleep(0.3)
                skill_lv_btn_x = ratioConvert(370)
                if IsColorAtCoord(skill_lv_btn_x, s.pos[1], CR_AtiveSkill_lvup_btn):
                    # autoit.mouse_click('left', tapmenu_skill_lvbtn_x, y, 1, 5)
                    uiAction.click(335, s.pos[1])
                    time.sleep(0.1)




    #
    #     y = tapmenu_btn_init_y - distance_btn_y
    #     for i, sk in enumerate(skill_list):
    #         y += distance_btn_y
    #
    #         # check diabled skill
    #         if sk[1] == 0:
    #             continue
    #
    #
    #     # check Mega boost
    #     if not IsColorAtCoord(hero_btn_x, tapmenu_megaboost_btn_y, c_megaboost):
    #         autoit.mouse_click('left', hero_btn_x, tapmenu_megaboost_btn_y, 1, 10)
    #
    #     bottomMenuExit()
    #
    # def cancelSkills():
    #     # open bottom menu
    #     bottomMenuExit()
    #     openBMenu(Icons.BMenu_Tap.name)
    #
    #     # sword master lv up
    #     autoit.mouse_click('left', hero_btn_x, swordmaster_btn_y, 1, 5)
    #
    #     distance_btn_y = 88
    #     y = tapmenu_btn_init_y - distance_btn_y
    #     for i in range(5):
    #         y += distance_btn_y
    #
    #         autoit.mouse_click('left', hero_btn_x, y, 1, 5)
    #
    #     time.sleep(1)
    #     bottomMenuExit()