def rgb(r, g, b):
    r = min(max(r, 0),255)
    g = min(max(g, 0),255)
    b = min(max(b, 0),255)
    return ('%02x%02x%02x' % (r, g, b)).upper()
