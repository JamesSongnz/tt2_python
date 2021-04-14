from data.constants import SCREEN_SCALE_RATIO


class Rect():

    x = 0
    y = 0
    w = 0
    h = 0

    scale = SCREEN_SCALE_RATIO

    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w =w
        self.h = h

    def scaleup(self):
        return int(self.x * self.scale),\
               int(self.y * self.scale) , \
               int(self.w * self.scale),\
               int(self.h * self.scale)

    def scaledn(self):
        return int(self.x / self.scale),\
               int(self.y / self.scale), \
               int(self.w / self.scale),\
               int(self.h / self.scale)


    def toString(self):
        return f' {self.x}, {self.y}, {self.w}, {self.h}'

    # def toStringf(self):
    #     return f'{Rect:%x %y %w %h}'


if __name__ == '__main__':
    r =Rect(0,0, 10, 10)
    print(r.toString())

    print (r.scaleup())
    print (r.scaledn())
