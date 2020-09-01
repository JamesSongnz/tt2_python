import autoit


def IsColorAtCoord(x, y, check_color):
    color = autoit.pixel_get_color(x, y )
    r = color >> 16 & 0xff
    g = color >> 8 & 0xff
    b = color & 0xff

    cr = check_color >> 16 & 0xff
    cg = check_color >> 8 & 0xff
    cb = check_color & 0xff

    offset = 0x0f

    if cr-offset <= r <= cr+offset and \
            cg-offset <= g <= cg+offset and \
            cb-offset <= b <= cb+offset:
        return True

    return False


def IsColorInVRange(x, y, color, yrange = 50, step=10):
    for i in range(0, yrange, step):
        if IsColorAtCoord(x, y + i, color):
            return True

    return False

def IsColorInRect(x, y, color, xrange, yrange, step = 2):
    xoffset = int(xrange / 2)
    yoffset = int(yrange / 2)

    for i in range(-xoffset, +xoffset, step):
        for j in range(-yoffset, +yoffset, step):
            if IsColorAtCoord(x + i, y + j, color):
                return True

    return False