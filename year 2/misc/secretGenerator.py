import string
from sys import argv
import random

def generate(length: int = 16):
    choices = ''.join([str(string.ascii_letters), str(string.digits), str(string.punctuation)])
    out = ''
    for i in range(length):
        temp = random.choice(choices)
        out += temp
    return out


if __name__ == "__main__":
    if len(argv) <= 1:
        print(generate())
    else:
        try:
            temp = int(argv[1])
            integer = True
        except TypeError:
            print("this should be a number dummy")
            exit()
        print(generate(temp))
