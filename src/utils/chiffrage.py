secret_key = "sdhfsyug_ètgduhfgyudstfeisyfgsyutfgs_çès-tdfcsiudgyzeçè-fyug"


# Table vérité XOR


# | A | B | A ⊕ B |
# |---|---|--------|
# | 0 | 0 |    0   |
# | 0 | 1 |    1   |
# | 1 | 0 |    1   |
# | 1 | 1 |    0   |


def encrypt(password: str):
    encryptedPassword = ""
    for i in range(len(password)):
        caractere_chiffre = chr(ord(password[i]) ^ ord(secret_key[i % len(secret_key)]))
        encryptedPassword += caractere_chiffre
    return encryptedPassword

def decrypt(password: str):
    return encrypt(password)


