from system_hotkey import SystemHotkey

from scenarios.Actions.ActiveSkillUp import ActiveSkillUp
from scenarios.Actions.prestiges import Prestige
from scenarios.Actions.testAction import testFunction

hk = SystemHotkey()


def register_hotkey():
    '''
    hk = SystemHotkeys()
    hk.register(('control', 'shift', 'h'), callback=lambda: print("Easy!"))
    hk.unregister(('control', 'shift', 'h'))
    '''
    #
    # hk.register(('control', 'shift', 's'), callback=autoSCStart)
    # hk.register(('control', 'shift', 'z'), callback=oneSCStart)
    # hk.register(('control', 'shift', 'x'), callback=autoHSStart)
    # hk.register(('control', 'shift', 'c'), callback=oneHSStart)
    # hk.register(('control', 'shift', 'w'), callback=rareSCStart)
    hk.register(('f4', 'f4', 'f4'), callback=testFunction)
    hk.register(('f3', 'f3', 'f3'), callback=newStartSkLvUp)
    # hk.register(('f6', 'f6', 'f6'), callback=goTapping)
    # hk.register(('control', 'shift', 'a'), callback=stopAutoing)
    # # hk.register(('control', 'shift', 'h'), callback=testFunction )
    #

    hk.register(('control', 'shift', 'e'), callback=exitFunction)
    hk.register(('control', 'shift', 'p'), callback=doPrestige)



def doPrestige(evt):
    p = Prestige()
    p.do()


def newStartSkLvUp(evt):
    s = ActiveSkillUp()
    s.do()

def exitFunction(evt):
    print('exit')

    global gAutoing
    print(f' exit, gauto ', {gAutoing})

    exit(0)
    try:
        hk.unregister(('control', 'shift', 'a'))
        hk.unregister(('control', 'shift', 's'))
        hk.unregister(('control', 'shift', 'e'))
    except:
        pass

    exit(0)


def getAutoing():
    global gAutoing
    print(f'get auto ', {gAutoing})
    return gAutoing

def stopAutoing(evt):
    global gAutoing
    print(f'Try Stop Auto Thread')
    gAutoing = not gAutoing
    print(f'toglle auto  ', {gAutoing})
