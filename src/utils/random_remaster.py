import time

def random():
    return int(str(time.time()).replace('.', '')[8:])


def randomRange(min, max):
    return int(str(time.time()).replace('.', '')[8:]) % (max - min) + min

