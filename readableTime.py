intervals = [
    ['years', 31536000],  # 60 * 60 * 24 * 7
    ['days', 86400],    # 60 * 60 * 24
    ['hours', 3600],    # 60 * 60
    ['minutes', 60],
    ['seconds', 1],
    ]
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        result = []
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        time = ', '.join(result[:])
        print(result)
        if len(time) > 9:
            time = ', '.join(result[:-1])
            time = time + ' and '
            time = time + str(result[-1])
            return time
        else:
            return time
