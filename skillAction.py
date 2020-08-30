from uiUtils import *


skill_coord = {'HS': 45, 'DS': 140, 'HM':240, 'FS':320, 'WC': 420, 'SC':520 }
skill_btn_y = 940


"""
    close bottom tap
    click skills
    args = skill order & kinds

"""
def useSkills(sks):
    bottomMenuExit()

    for i in range(2):
        for sk_name in sks:
            useSkill(sk_name)

"""
    close bottom tap
    click skills
    args = skill order & kinds

"""
def useAllSkills(sks):
    bottomMenuExit()

    for i in range(5):
        for key in skill_coord:
            useSkill(key)

def useSkill(at):
    autoit.mouse_click("left", skill_coord[at], skill_btn_y)


def useAllSkillsButHS():
    sks = ['DS', 'HM', 'FS', 'WC', 'SC']
    useSkills(sks)

    ''' 
    
    ; check up right x icon
    Local $left = 655, $top = 55,   $right =687 , $bottom = 76
	Local $TapOpenIconCheckSum = 122565676;


    Local $pixelCheck =0
    $pixelCheck = PixelCheckSum( $left, $top, $right, $bottom)
	ConsoleWrite(  " check tap : " & $pixelCheck & @CRLF)

    If $TapOpenIconCheckSum <> $pixelCheck Then
        Return False
    Else
        Return True
    EndIf
    '''