
import time

def random():
    return int(str(time.time()).replace('.', '')[8:])


def randomRange(min, max):
    taille_echantillon = 1000
    amplitude = 1.0
    time.sleep(0.03)
    return int(str(generer_bruit_blanc(taille_echantillon, amplitude)[int(str(random())[-1])]).replace('.', '')[8:]) % (max - min) + min


def generer_bruit_blanc(taille_echantillon, amplitude=1.0):
    seed = int(time.time() % 2**32)
    state = (seed * 6364136223846793005 + 1) & 0xFFFFFFFFFFFFFFFF  # Générateur congruentiel linéaire

    bruit = []

    for _ in range(taille_echantillon):
        state = (state * 6364136223846793005 + 1) & 0xFFFFFFFFFFFFFFFF
        valeur_aleatoire = ((state >> 33) & 0xFFFFFFFF) / 0xFFFFFFFF  # Normalisation de [0, 1]
        bruit.append(valeur_aleatoire * amplitude)

    return bruit


print(randomRange(1, 100))
print(randomRange(1, 100))
print(randomRange(1, 100))
print(randomRange(1, 100))



