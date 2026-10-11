import os
import time

RESET = '\u001b[0m'

def pattern_g(c1, c2):
    PURPLE = f'\u001b[48;5;{c1}m'
    CYAN   = f'\u001b[48;5;{c2}m'
    size = 5
    for i in range(-size, size + 1):
        line = ''
        for j in range(-size, size + 1):
            if abs(i) + abs(j) <= size:
                line += PURPLE + '  ' + RESET
            else:
                line += '  '
        for j in range(-size, size + 1):
            if abs(i) + abs(j) <= size:
                line += CYAN + '  ' + RESET
            else:
                line += '  '
        print(line)

def animate():
    colors = [(93, 51), (226, 196), (46, 201), (129, 21)]
    while True:
        for c1, c2 in colors:
            os.system("cls")
            pattern_g(c1, c2)
            time.sleep(0.7)

animate()