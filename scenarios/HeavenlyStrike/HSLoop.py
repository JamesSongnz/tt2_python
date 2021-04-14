
def HSLoop():
    global cur_action, hs_hit_cnt, cur_hsafter_action
    constants.Stucked_check_count = 15

    # print(f' HSLoop, gauto ', {m.getAutoing()})
    # check play screen status
    turnPlayScreen()

    # use skills
    #   activate all skills,  but keep DS as 1 : it is not grant any damage increase
    skillAction.useAllSkillsButHS()

    # HS use
    #   only when mana is enough
    # if enoughMana():
    # used = skillAction.spamHS() if enoughMana('HS') else 0
    # check other essential skill is active
    used = False


    if enoughMana('HS'):
        mode = 'spamming'
        if skillAction.readySpam():
            used = skillAction.spamHS()

    else:
        mode = 'otheraction'

    print(f'HS loop: used 1, cur_act 2, hs hit cnt 3, cur_hsafter_action  4', {used}, {cur_action}, {hs_hit_cnt}, {cur_hsafter_action})

    # wait for next HS
    if 'spamming' == mode:
        posionDaggerAtOnce()
        # click pet
        tapClanmate()
        tapPetMoney()

        hs_hit_cnt += 1

        # mix other actions while spamming
        if hs_hit_cnt > constants.HS_Spamming_Keep_cnt:
            hs_hit_cnt = 0
            hsafter_action = hs_after_actions[cur_hsafter_action]
            doOtherAction(hsafter_action)
            cur_hsafter_action = 0 if cur_hsafter_action >= len(hs_after_actions) - 1 else cur_hsafter_action + 1
        else:
            # catch fairy on moving area tap 1 sec
            tap(487, 299)
            for i in range(8):
                tapCursor()

            time.sleep(0.9)
    else:   # not enough mana -> do other action to wait fill mana

        # not used . do other action one at a time
        pass

        # check prestige & restart active skills
        """
        other_action = other_actions[cur_action]

        doOtherAction(other_action)
        cur_action = 0 if cur_action >= len(other_actions)-1 else cur_action + 1
        hs_hit_cnt = 0  # clear to restart spamming
        time.sleep()  # wait a little until refill mana

        """

        # time.sleep(3)  # wait a little until refill mana
        # catch fairy on moving area tap 1 sec
        catchFairy()
        # time.sleep(0.9)

    if checkPrestige():
        global restart
        lvupActiveSkill('HS')
        restart = True

    # move cursor to indicate loop action is over
    tap(325, 780)


