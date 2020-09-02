import autoit

import uiUtils
from constants import skill_coord, skill_btn_ready_y, skill_btn_y, skill_btn_active_y

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

# ret : True when sucess
def useSkill(at):
    if checkReadyBtn(at):
        autoit.mouse_click("left", skill_coord[at], skill_btn_y)
        return True
    return False

def checkSkillActive(at):
    return checkSkillStatus(at, 'active')

def checkReadyBtn(at):
    return checkSkillStatus(at, 'ready')


def checkSkillStatus(at, state='ready'):
    x = skill_coord[at]
    if state == 'ready':
        y = skill_btn_ready_y
        state_color = 0xffffff
    else: # active
        y = skill_btn_active_y
        state_color = 0xffae00

    for i in range(4):
        color = autoit.pixel_get_color(x, y + i)
        if color == state_color:
            return True
    return False


# only when SC, FS, WC is active. spam is available
def readySpam():
    if checkSkillActive('SC') and checkSkillActive('FS') and checkSkillActive('WC'):
        return True
    return False

def useAllSkillsButHS():
    sks = ['SC', 'FS', 'WC', 'HM', 'DS']
    useSkills(sks)

# use HS,
# return whether used or failed
def spamHS():
    return useSkill('HS')