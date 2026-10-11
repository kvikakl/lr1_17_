import os

RED   = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'

def flag():
    width  = 20
    height = 10
    pixel  = '  '

    cx = width / 2 - 0.5
    cy = height / 2 - 0.5
    R  = height / 3

    for i in range(height):
        line = ''
        for j in range(width):
            if (j - cx) ** 2 + (i - cy) ** 2 <= R ** 2:
                line += RED + pixel
            else:
                line += WHITE + pixel
        print(line + RESET)

flag()