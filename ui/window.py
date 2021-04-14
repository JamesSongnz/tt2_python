import autoit

from data.constants import ClientClass, Client


def activateWindow():
    # window align
    autoit.win_activate(ClientClass)
    autoit.win_move(Client, 0, 0)
