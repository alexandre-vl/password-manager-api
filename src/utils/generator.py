from src.utils.random_remaster import randomRange
import time

chars = "AZERTYUIOPQSDFGHJKLMWXCVBN"
special_chars = "&*$%!:.,?#@+="

def generate(
    size: int = 16,
    need_chars: bool = True,
    need_special_chars: bool = True
):
    started_time = time.time()

    chars_ratio = 0.6
    number_ratio = 0.4
    special_chars_ratio = 0.2

    generatedPassword = ""
    for i in range(size):
        time.sleep(00.1)
        if randomRange(0, 10) <= special_chars_ratio * 10: # Use special chars
            generatedPassword += special_chars[randomRange(0, len(special_chars))]
        elif randomRange(0, 10) <= number_ratio * 10: # Use number
            generatedPassword += str(randomRange(0, 9))
        elif randomRange(0, 10) >= chars_ratio * 10: # Use normal chars
            generatedPassword += chars[randomRange(0, len(chars))]

    print(f'Generation takes {time.time() - started_time}ms')
    return generatedPassword 

print(generate())