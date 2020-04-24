# Implementation of Bresenham's Lin Drawing algorithm
# See: https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm


def PlotLine(x0, x1, y0, y1):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            return _plotShallow(x1, x0, y1, y0)
        else:
            return _plotShallow(x0, x1, y0, y1)
    else:
        if y0 > y1:
            return _plotSteep(x1, x0, y1, y0)
        else:
            return _plotSteep(x0, x1, y0, y1)

def _plotShallow(x0, x1, y0, y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2 * dy - dx
    y = y0
    ret = []
    for x in range(x0, x1 + 1):
        ret.append((x, y))
        if D > 0:
            y += yi
            D -= 2 * dx
        D += 2 * dy
    return ret

def _plotSteep(x0, x1, y0, y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x0
    ret = []
    for y in range(y0, y1 + 1):
        ret.append((x, y))
        if D > 0:
            x += xi
            D -= 2 * dy
        D += 2 * dx
    return ret