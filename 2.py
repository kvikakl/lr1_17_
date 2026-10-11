import time

PURPLE = '\u001b[48;5;93m'
CYAN   = '\u001b[48;5;51m'
RESET  = '\u001b[0m'

def pattern_g():
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

for k in range(3):
    pattern_g()
    print()
    time.sleep(1)
    