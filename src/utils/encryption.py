secret_key = "sdhfsyug_ètgduhfgyudstfeisyfgsyutfgs_çès-tdfcsiudgyzeçè-fyug"


# Bit Value          (Decimal)	8	4	2	1
# 10                 (1010)	    1	0	1	0
# 6                  (0110)	    0	1	1	0
# XOR Result         (1100)	    1	1	0	0


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
        caractere_chiffre = chr(ord(password[i]) + ord(secret_key[i % len(secret_key)]))        # ^ signifie qu'on appelle xor
        encryptedPassword += caractere_chiffre
    return encryptedPassword


def decrypt(password: str):
    encryptedPassword = ""
    for i in range(len(password)):
        caractere_chiffre = chr(ord(password[i]) - ord(secret_key[i % len(secret_key)]))
        encryptedPassword += caractere_chiffre
    return encryptedPassword

    
# var = encrypt('pass')
# var2 = decrypt(var)
# print(var)
# print(var2)
