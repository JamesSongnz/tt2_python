import time

from autoit import autoit

from data.constants import icon_tables_e
from ui.uiUtils import menuMakeFull


class Cmd:
    """ base class for cmds"""
    action = 1


    def doAction(self):
        """ do something """




class OpenBtmMenu(Cmd):

    def doAction(self, menu):
        """ open """
        self.openBMenu(menu)

    def openBMenu(menu):
        x, y, _, _ = icon_tables_e[menu]
        autoit.mouse_click('left', x, y, 1, 10)
        time.sleep(0.6)

        menuMakeFull()
