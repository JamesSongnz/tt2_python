# pip install pyautogui


import cv2 as cv
import numpy as np
import pyautogui

from data.constants import icon_tables_e, Icons, icon_files_e
from data.coordinates import Image_coords
from data.utils import ratioConvertIcon


def IsExistBtn(ImageEnum):
    return _IsExistBtn(ImageEnum.coord, ImageEnum.img)




def _IsExistBtn(btn_pos, imgfile):

    print(f' Is exit btn {btn_pos} , {imgfile}')
    img_piece = cv.imread(imgfile, cv.IMREAD_COLOR)
    h, w = img_piece.shape[:2]


    pic = pyautogui.screenshot(region=btn_pos)

    # pic = pyautogui.screenshot(region=(0, 0, 720, 1280+60))
    img_frame = np.array(pic)
    img_frame  = cv.cvtColor(img_frame, cv.COLOR_RGB2BGR)

    meth = 'cv.TM_CCOEFF_NORMED'
    method = eval(meth)

    res = cv.matchTemplate(img_piece, img_frame, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    #cv.rectangle(img_frame, top_left, bottom_right, (0, 255, 0), 2)
    print(max_val, top_left)

    # cv.imshow('result', img_frame)
    return max_val > 0.9

if __name__ == "__main__":
    # if IsExistBtn(Icons.Menu_Make_FUll.name,"../imgs/btn_menuexit.png"):
    if _IsExistBtn(Image_coords.Bottom_Menu_X_Half.coord,"../imgs/btn_menuexit.png"):

    # if IsExistIcon(Icons.Menu_Make_FUll.name):
        x, y, _, _ = icon_tables_e[Icons.Menu_Make_FUll.name]
        print("found!!!")
    else:
        print("not found")

    import time
    time.sleep(3)

