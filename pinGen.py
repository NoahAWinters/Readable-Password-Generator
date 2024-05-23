import random
import string


def pin_gen(length=4):
    pin = ""
    for x in range(length):
        pin += random.choice(string.digits)

    return pin


pin = pin_gen()
print(pin)
