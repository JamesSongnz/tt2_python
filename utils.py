import autoit


# find color at pos with  color range
def IsColorAtCoord(x, y, check_color, offset=0x0f):
    color = autoit.pixel_get_color(x, y)
    # print(f'        color at ', {x}, {y}, {hex(color)})
    r = color >> 16 & 0xff
    g = color >> 8 & 0xff
    b = color & 0xff

    cr = check_color >> 16 & 0xff
    cg = check_color >> 8 & 0xff
    cb = check_color & 0xff

    if cr-offset <= r <= cr+offset and \
            cg-offset <= g <= cg+offset and \
            cb-offset <= b <= cb+offset:
        return True

    return False

# find one color element from r g b  at x y position
def IsOneColorAtCoord(x, y, one_color, offset=0xf):
    color = autoit.pixel_get_color(x, y )
    r = color >> 16 & 0xff
    g = color >> 8 & 0xff
    b = color & 0xff

    # check comparing one color
    cr = one_color >> 16 & 0xff
    cg = one_color >> 8 & 0xff
    cb = one_color & 0xff

    pc = r if cr!=0x00 else (g if cg!=0x00 else b)
    oc = cr if cr!=0x00 else (cg if cg!=0x00 else cb)

    return True if oc - offset <= pc <= oc + offset else False

def IsOneColorInVRange(x, y, one_color, yrange = 50, step=10, offset=0xf):

    for i in range(0, yrange, step):
        if IsOneColorAtCoord(x, y + i, one_color, offset):
            return True

    return False


def IsColorInVRange(x, y, color, yrange = 50, step=10, offset=0xf):
    for i in range(0, yrange, step):
        if IsColorAtCoord(x, y + i, color, offset):
            return True

    return False

# return offset of y
def findColorInVRange(x, y, color, yrange = 50, step=10, offset=0xf):
    for i in range(0, yrange, step):
        if IsColorAtCoord(x, y + i, color, offset):
            return i

    return -1

def IsColorInRect(x, y, color, xrange, yrange, step = 2):
    xoffset = int(xrange / 2)
    yoffset = int(yrange / 2)

    for i in range(-xoffset, +xoffset, step):
        for j in range(-yoffset, +yoffset, step):
            if IsColorAtCoord(x + i, y + j, color, offset=0x2f):
                return True

    return False

