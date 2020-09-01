
import enum


# UI utils
class Icons(enum.Enum):
    Bottom_Menu_X_Full = enum.auto()
    Bottom_Menu_X_Half = enum.auto()
    # b menu
    BMenu_Tap = enum.auto()
    BMenu_Heroes = enum.auto()
    BMenu_Equip = enum.auto()
    BMenu_Pet = enum.auto()

    Menu_Make_FUll = enum.auto()

class Positions(enum.Enum):
    BMenuWheel = enum.auto()
    RelicsOnPlayScr = enum.auto()



pos_tables = \
    {
        Positions.BMenuWheel.name: (241, 740),
        Positions.RelicsOnPlayScr.name: (35, 685),

    }


icon_tables_e = \
    {
#        Icons.RIGHT_X.name: {'x': 655, 'y': 55, 'x2': 687, 'y2': 76},
        Icons.Bottom_Menu_X_Full.name: (510, 48, 535, 60),
        Icons.Bottom_Menu_X_Half.name: (510, 585, 535, 602),

        # bottom menu
        Icons.BMenu_Tap.name: (45, 1025, 0, 0),
        Icons.BMenu_Heroes.name: (145, 1025, 0, 0),
        Icons.BMenu_Equip.name: (235, 1025, 0, 0),
        Icons.BMenu_Pet.name: (325, 1025, 0, 0),

        Icons.Menu_Make_FUll.name: (430, 590, 465, 600)
    }

icon_checksums_e = \
    {
        Icons.Bottom_Menu_X_Full.name: 1531251295,
        Icons.Bottom_Menu_X_Half.name: 1952088816,

        Icons.Menu_Make_FUll.name: 1823557018
    }


# tapping
click_coord_table = \
    {
        'tapping': (310, 525),
        'pet': (335, 510),
        'petburst': (285, 455),
        'clanmate': (215, 545),
        'menufullexit': (561, 44),
        'menuharfexit': (525, 595),
        'fairystart': (80, 280),
        'fairyend': (580, 280),
        'fairycollect': (500, 774),
    }

# colors for comparasion
CR_Dagger = 0x4a8429
CR_AtiveSkill_lvup_btn = 0xc72b29
CR_ActiveSkill_btn = 0xef6e14
# skills
skill_coord = {'HS': 45, 'DS': 140, 'HM': 234, 'FS': 328, 'WC': 420, 'SC': 517 }
skill_btn_y = 940
skill_btn_ready_y = 898

# menu


# buttons
# tap menu
swordmaster_btn_y = 208
tapmenu_skill_lvbtn_x = 370
tapmenu_megaboost_btn_y = 977
c_megaboost = 0x494849
tapmenu_btn_init_y = 451

# heroes
hero_btn_x = 548  # rightmost of btn
hero_btn_init_y = 210
hero_btn_activated_check_y = 165