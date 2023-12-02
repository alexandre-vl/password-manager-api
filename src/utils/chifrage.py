class Chiffrement:
    def __init__(self):
        self.author = 'La Team Alexandre'
        self.version = '0.0.1'

    def encrypt(self, message, key, ascii, iicsa):
        bin_string = ''
        scrambled = ''

        for letter in range(len(message)):
            bin_string += ascii[message[letter]]

        ascii_blocks = []
        for block in range(len(bin_string) // 8):
            ascii_blocks.append('')

        ascii_block = 0
        for bit in range(len(bin_string)):
            ascii_blocks[ascii_block] += bin_string[bit]

            if len(ascii_blocks[ascii_block]) == 8:
                ascii_block += 1

        for char in message:
            print(char, ascii[char])

        for bit in range(len(bin_string)):
            scrambled += str(int(bin_string[bit]) ^ int(key[bit]))

        bytes = []
        for bit in range(len(scrambled) // 8):
            bytes.append('')

        byte = 0
        for bit in range(len(scrambled)):
            bytes[byte] += scrambled[bit]

            # parse by byte
            if len(bytes[byte]) == 8:
                byte += 1

        return scrambled

    def decrypt(self, scrambled, ascii, iicsa, key):
        decrypted = ''

        for k in range(len(scrambled)):
            decrypted += str(int(scrambled[k]) ^ int(key[k]))


        blocks = []
        for block in range(len(scrambled) // 8):
            blocks.append('')


        block = 0
        for letter in range(len(decrypted)):
            blocks[block] += decrypted[letter]


            if len(blocks[block]) == 8:
                block += 1

        decrypted_message = ''

        for byte in range(len(blocks)):
            decrypted_message += iicsa[blocks[byte]]

        return


# ch = Chiffrement()
# var = ch.encrypt('blabla', 'pass')
# print(var)
# print(ch.decrypt(var, 'pass'))


