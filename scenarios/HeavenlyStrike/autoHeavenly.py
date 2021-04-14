from threading import Thread

#from main import gAutoing
import main as m

restart = True
start_time = 0

def autoHSStart(evt):
    SCThread = Thread(target=autoHS, args=(1,))
    # not work SCThread.daemon = True
    SCThread.setDaemon(True)
    SCThread.start()
    #SCThread.join()


def oneHSStart(evt):
    m.activateWindow()
    HSLoop()

def autoHS(arg):
    #global gAutoing
    global restart

    while m.getAutoing():
        restart = False # started
        HSLoop()
        fastPrestigeTimeCheck()

cur_action = 0
other_actions = ['fairy', 'heroes', 'fairy', 'heroes', 'helmet']
# other_actions = ['fairy', 'heroes', 'dagger','dagger', 'fairy', 'heroes', 'helmet']
hs_after_actions = ['hero_helmet', 'heroes', 'heroes']
hs_hit_cnt = 0

cur_hsafter_action = 0



