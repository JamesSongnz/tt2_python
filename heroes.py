
'''
    lv up latest heroes
'''
import time

import autoit

from uiUtils import bottomMenuExitFull, Icons, openBMenu, menuScrollUp, bottomMenuExit

import enum

''' 
class BMenus(enum.Enum):
    Tap = enum.auto()
    Heroes = enum.auto()
    Equip = enum.auto()
    Pet = enum.auto()
'''

hero_btn_x = 470
hero_btn_init_y = 210

def heroLeveling():

    print(f'Hero lv up')

    # open bottom menu
    bottomMenuExit()
    openBMenu(Icons.BMenu_Heroes.name)

    # scroll up
    menuScrollUp()

    # click lv up btn
    y = hero_btn_init_y # 530 - 170 = 360 , 360/4 =
    for i in range(5):
        for j in range(4):
            autoit.mouse_click('left', hero_btn_x, y, 1, 5)
            time.sleep(0.1)
        y += 90

    bottomMenuExit()

    '''
    Func UpHeroLv()
	$g_autoing = True
	ToolTip('Up Hero  ontime start "', 0,0)

	TapStop()
	BottomMenuExit()

	; open hero menu
	OpenMenu($eHeroM)
	Sleep(100)

	MenuScrollUp2()
	ScrollTopAlign()

	;; high H  twice up
	HeroLvUpOnScrFast(4,4)
	For $i = 1 To 4 Step 1
		HeroLvUpOnScrFast(4,4)
		;; scrooll
		Sleep(100)
		ScrollHeroMDown()
		Sleep(100)
	Next
	; last lv up
	HeroLvUpOnScrFast(4,4)

	;; up to top
	MenuScrollUp2()
	MenuScrollUp2()

	; close menu
	BottomMenuExit()

		; move screen center
	MouseClick("left", $screen_click_x, $screen_click_y)
	TapStart()
EndFunc
    :return: 
    '''