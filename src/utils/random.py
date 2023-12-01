import time


def now():
    nowTime = time.time()
    return int(nowTime * 1000)


def random(size: int):
    numberListe = []
    numberInt = ''
    for i in range(size):
        nowMiliTime = str(now())
        numberListe.append(nowMiliTime[-1])
        sleep = int(numberListe[i]) / 20
        time.sleep(sleep)
    for i in numberListe:
        numberInt += i
    return numberInt


def randint(start: int = 0, stop: int = 10):
    size = start + stop
    value = random(len(str(size)))
    if int(value) > stop:
        return random(len(str(start)))

    elif int(value) < start:
        return random(len(str(stop)))

    else:
        return int(value)


# print(randint(start=0, stop=20))
