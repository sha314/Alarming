

class Converters:
    def __init__(self):
        print("Converters.__init__")

    def to_seconds(self, timestr):
        seconds = 0
        for part in timestr.split(':'):
            seconds = seconds * 60 + int(part)
        return seconds

    def seconds_to_hhmmss(self, seconds):
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

        return "{:2}:{:2}:{:2}".format(hr, minute, r)
