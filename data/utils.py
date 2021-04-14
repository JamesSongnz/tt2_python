

def ratioConvertTuple(t, ratio):
    ''' tuple (x, y x2, y2) '''
    tl = list(t)
    tl2 = [int(i * ratio)  for i in tl]
    return tuple(tl2)

def ratioConvert(x, ratio=1.25):
    return int(x*ratio)


def ratioConvertIcon(t):
    ''' tuple (x, y x2, y2) '''
    # tp = ()
    tl = list(t)
    tl2 = [ int(i*1.5)  for i in tl]
    #tp = (int(i*1.5) for i in t)
    # print(f'--t p {tl2}')
    # for i in tl2:
    #     print(i)

    return tuple(tl2)
