

def to_seconds_f2(timestr="0h1m3s"):
    # timestr = timestr.split()  # get rid of spaces

    separators = ['h', 's', 'm']
    hour_str = "0h"
    min_str = "0h"
    sec_str = "0h"
    hour = 0
    minutes = 0
    seconds = 0
    if 'h' in timestr:
        hour = int(timestr.split('h')[0])
        print(hour)
        hour_str = "{}h".format(hour)
    else:
        timestr = "{}{}".format(hour_str, timestr)

    print(timestr)
    if 'm' in timestr:
        ss = timestr.split('h')[1]
        minutes = int(ss.split('m')[0])
        print(minutes)
        min_str = "{}m".format(minutes)
    else:
        timestr = "{}{}{}".format(hour_str, min_str, timestr)

    print(timestr)
    if 's' in timestr:
        ss = timestr.split('h')[1]
        ss = timestr.split('m')[1]
        seconds = int(ss.split('s')[0])
        print(seconds)

    print("{}:{}:{}".format(hour, minutes, seconds))

    return hour*3600 + minutes*60 + seconds


def to_seconds(timestr):
    seconds = 0
    for part in timestr.split(':'):
        # print(part)
        # print(type(part))
        seconds = seconds * 60 + int(part)
    return seconds

def seconds_to_hhmmss(seconds):
    r = seconds
    timestamp = ""

    hr = int(r / 3600)
    r = r % 3600
    print(r)
    print(hr)

    minute = int(r / 60)
    r = r % 60
    print(r)
    print(minute)

    return "{:02}:{:02}:{:02}".format(hr, minute, r)


if __name__ == '__main__':
    # print(to_seconds_f2('23s'))
    print(to_seconds("1:1:42"))
    print(seconds_to_hhmmss(7200+65+3))


