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

def addition_binary(a, b):
    string_a = str(a)[::-1]
    string_b = str(b)[::-1]
    is_retenu = False
    
    final = ""
    
    for i in range(len(string_a) if len(string_a) >= len(string_b) else len(string_b)):
        to_a = string_a[i] if len(string_a) -1 >= i else "0"
        to_b = string_b[i] if len(string_b) -1 >= i else "0"

        print('_________IN___________')
        print('i: ', i)
        print('to_a: ', to_a)
        print('to_b: ', to_b)
        print('result: ', simple_add(to_a, to_b))
        print('retenu: ', is_retenu)
        print('final: ', final)

        if len(final) > 0 and final[0] == "1" and to_a == "1" and to_b == "0":
            is_retenu = False
        
        if is_retenu:
            final = "1" + final
            is_retenu = False


        
        else:
            if to_a == to_b and to_a == "1":
                final += "0"
                is_retenu = True
            else:
                final = str(simple_add(to_a, to_b)) + final

        print('_________OUT___________')
        print('i: ', i)
        print('to_a: ', to_a)
        print('to_b: ', to_b)
        print('result: ', simple_add(to_a, to_b))
        print('retenu: ', is_retenu)
        print('final: ', final)
    print(is_retenu)
    return final


def simple_add(a, b):
    if a == "0":
        if b == "0":
            return 0
        else: return 1
    else: 
        if b == "0":
            return 1
        else: return 0

print(addition_binary(1011, 1))



