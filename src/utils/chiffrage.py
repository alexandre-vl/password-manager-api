# Create two functions to encrypt and decrypt a password with a salt and a pepper using sha56 algorithm without any import and without hashlib library

import random
import string

def generate_salt():
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return salt

def generate_pepper():
    pepper = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return pepper

# Make the encryption more secure
def encrypt(salt, pepper, password):
    encrypted_password = salt + password + pepper
    return encrypted_password

def decrypt(salt, pepper, encrypted_password):
    decrypted_password = encrypted_password.replace(salt, '').replace(pepper, '')
    return decrypted_password

def sha56():
    


def main():
    my_password = "bonjour"

    salt = generate_salt()
    pepper = generate_pepper()

    encrypted_password = encrypt(salt, pepper, my_password)
    print(encrypted_password)

    decrypted_password = decrypt(salt, pepper, encrypted_password)
    print(decrypted_password)



main()


