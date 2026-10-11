def sequence():
    file = open('sequence.txt', 'r')
    more = 0
    less = 0
    for line in file:
        num = float(line)
        if num < 0:
            if num > -5:
                more += 1
            elif num < -5:
                less += 1
    file.close()

    total = more + less
    p_more = more / total * 100
    p_less = less / total * 100

    print(f"Больше -5: {more} ({p_more:.1f}%)")
    print(f"Меньше -5: {less} ({p_less:.1f}%)")
    print()
    print("Диаграмма:")
    print("Больше -5: " + "█" * int(p_more / 2))
    print("Меньше -5: " + "█" * int(p_less / 2))
sequence( )