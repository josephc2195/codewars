def make_readable(seconds):
    s = seconds % 60
    m = int((seconds - s) / 60 % 60)
    h = int(((seconds - s) - (m * 60)) / 3600)
    return "{:02d}:{:02d}:{:02d}".format(h,m,s)
