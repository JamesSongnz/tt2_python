import autoit

import uiUtils
from constants import skill_coord, skill_btn_ready_y, skill_btn_y

"""
    close bottom tap
    click skills
    args = skill order & kinds

"""
def useSkills(sks):
    uiUtils.bottomMenuExit()

    for i in range(2):
        for sk_name in sks:
            useSkill(sk_name)

"""
    close bottom tap
    click skills
    args = skill order & kinds

"""
def useAllSkills(sks):
    uiUtils.bottomMenuExit()

    for i in range(5):
        for key in skill_coord:
            useSkill(key)

def useSkill(at):
    if checkReadyBtn(at):
        autoit.mouse_click("left", skill_coord[at], skill_btn_y)


def checkReadyBtn(at):
    x = skill_coord[at]
    color = autoit.pixel_get_color(x, skill_btn_ready_y)

    if color == 0xffffff:
        return True
    return False


def useAllSkillsButHS():
    sks = ['DS', 'HM', 'FS', 'WC', 'SC']
    useSkills(sks)

