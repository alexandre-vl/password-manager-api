import time


def now():
    nowTime = time.time()
    return int(nowTime * 1000)


def randint(size: int):
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


print(randint(size=2))
