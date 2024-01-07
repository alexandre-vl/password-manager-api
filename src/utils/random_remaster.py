
import time


# Fonction qui génère un nombre pseudo-aléatoire basé sur le temps actuel
def random():
    return int(str(time.time()).replace('.', '')[8:])


# Fonction qui génère un échantillon de bruit blanc
def generer_bruit_blanc(taille_echantillon, amplitude=1.0):
    seed = int(time.time() % 2**32)                 # Exemple de seed 1704196143 le 02/01/2024 a 12:49
    # Constante 0xFFFFFFFFFFFFFFFF représente le nombre hexadécimal qui a tous ses bits à 1. En binaire = 64 bits à 1.
    state = (seed * 6364136223846793005 + 1) & 0xFFFFFFFFFFFFFFFF  # Générateur congruentiel linéaire pseudo aleatoire

    bruit = []

    for _ in range(taille_echantillon):
        state = (state * 6_364_136_223_846_793_005 + 1) & 0xFFFFFFFFFFFFFFFF
        valeur_aleatoire = ((state >> 33) & 0xFFFFFFFF) / 0xFFFFFFFF
        # Pour s'assurer que les bits au-delà des 32 premiers sont tous à zéro
        bruit.append(valeur_aleatoire * amplitude)

    return bruit


# Fonction qui génère un nombre aléatoire dans la plage spécifiée [min, max]
def randomRange(min, max):
    taille_echantillon = 1000
    amplitude = 1.0
    time.sleep(0.03)  # Pause pour garantir une différence de temps entre chaque appel
    return int(str(generer_bruit_blanc(taille_echantillon, amplitude)[int(str(random())[-1])]).replace('.', '')[8:]) % (max - min) + min


# Affiche quatre nombres aléatoires dans la plage [1, 100]
print(randomRange(1, 100))
print(randomRange(1, 100))
print(randomRange(1, 100))
print(randomRange(1, 100))
