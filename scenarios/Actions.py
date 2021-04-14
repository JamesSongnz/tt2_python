
def doOtherAction(other_action):
    print(f' HS : do others ', {other_action})
    if other_action == 'fairy':
        # catch fairy
        # catchFairy('short') # short version
        pass
    elif other_action == 'heroes':
        tapPetMoney()   # get money before heroes lv up
        # heroes lv up
        heroLeveling()
    elif other_action == 'dagger':
        # posing dagger
        #   only do when stucked more than once at the same stage
        #if getStuckedState():
        posionDaggerAtOnce()
    elif other_action == 'helmet':
        # set hero type equip
        #  move into hero leveling ()
        # changeHelmet()
        pass
    elif other_action == 'hero_helmet':
        heroLeveling()
        # move into hero leveling  changeHelmet()
    else:
        pass




def enoughMana(mode):
    # check mana bar
    if mode == 'HS':
        # 112, 839
        x = constants.ManaEnoughHS_x
        y = constants.ManaBar_y
        if IsOneColorInVRange(x, y, one_color=0xff, yrange = 10, step = 2):
            # has enough mana
            print('HS : has!!  enough Mana ')
            return True
        else:
            print('HS : not enough Mana ')


    return False

