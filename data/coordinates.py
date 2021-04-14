import enum

from data import constants
from data.constants import SCREEN_SCALE_RATIO
from data.utils import ratioConvertTuple


class Icons_coord(enum.Enum):
    # b menu
    BMenu_Tap = (45, 1030, 'z')
    BMenu_Heroes = (145, 1030 , 'x')
    BMenu_Equip = (235, 1030, 'c')
    BMenu_Pet = (325, 1030, 'v')

    IPanel_Half_x = (539, 610)
    IPanel_Full_x = (539, 57)
    IPanel_Make_Full = (460, 610)

    # Prestige
    Prestige_Panel_Btn = (478, 338)
    Prestige_Window_Btn = (290, 970)
    Prestige_Confirm_Btn = (390, 810)

    # Tap panel
    Tap_Sword_lv_Btn  = (482,215)

    def __init__(self, x, y, sk=None):
        self.ratio = 1.25
        self.point = (x, y)
        self.sk = sk

    @property
    def scaleup(self):
        return ratioConvertTuple(self.point, self.ratio)

    @property
    def pos(self):
        if constants.SCREEN_SCALE_RATIO != 1:
            return self.scaleup
        else:
            return self.point


class Image_coords(enum.Enum):
    Bottom_Menu_X_Full = (659, 58, 30, 30, "./imgs/btn_menuexit.png")
    Bottom_Menu_X_Half = (659, 750, 30, 30, "./imgs/btn_menuexit.png")
    Menu_Make_FUll = (430, 590, 465, 600)

    def __init__(self, x, y, w, h, img = None):
        self.ratio = 1.25
        self.rect = (x, y, x+w, y+h)
        self.img = img



    @property
    def scaleup(self):
        return ratioConvertTuple(self.rect, self.ratio)


    @property
    def scaledown(self):
        return ratioConvertTuple(self.rect, ratio=0.8)

    @property
    def coord(self):
        if constants.SCREEN_SCALE_RATIO != 1:
            return self.scaledown
        else:
            return self.rect