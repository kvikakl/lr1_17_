import os

RESET = '\u001b[0m'
GREEN = '\u001b[42m'
BLUE  = '\u001b[44m'

def graph():
    height = 15
    width  = 25
    pixel  = ' '

    for i in range(height, -1, -1):
        line = ''
        for j in range(width):
            y_graph = height - i       # от 0 до 15
            x_graph = j                # от 0 до 25

            if j == 0 or i == height:
                line += BLUE + pixel + RESET
            elif abs(y_graph - x_graph * 0.6) < 0.8:
                line += GREEN + pixel + RESET
            else:
                line += pixel
        print(line + RESET)

graph()