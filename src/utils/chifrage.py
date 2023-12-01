class Chiffrement:
    def __init__(self):
        self.author = 'La Team Alexandre'
        self.version = '0.0.1'

    def encrypt(self, password: str, key: str):
        encryptedPassword = ""
        for i in range(len(password)):
            caractere_chiffre = chr(ord(password[i]) ^ ord(key[i % len(key)]))
            encryptedPassword += caractere_chiffre
        return encryptedPassword

    def decrypt(self, password: str, key: str):
        return self.encrypt(password, key)


# ch = Chiffrement()
# var = ch.encrypt('blabla', 'pass')
# print(var)
# print(ch.decrypt(var, 'pass'))
print('(')


