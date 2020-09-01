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