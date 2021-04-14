from data.constants import SCREEN_SCALE_RATIO


class Point():
    ''' base point '''

    x = 0
    y = 0

    scale = SCREEN_SCALE_RATIO

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def click(self):
    #     clickPoint(self)

    def scaleup(self):
        return int(self.x * self.scale),\
               int(self.y * self.scale)


    def scaledn(self):
        return int(self.x / self.scale),\
               int(self.y / self.scale)


    def toString(self):
        return f' {self.x}, {self.y}, {self.w}, {self.h}'
