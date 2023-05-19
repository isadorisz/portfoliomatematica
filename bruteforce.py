from random import randint, choice

while(True):
    d1 = randint(0, 5) + 1
    d2 = randint(0, 5) + 1
    d3 = randint(0, 5) + 1
    d4 = randint(0, 5) + 1
    d5 = randint(0, 5) + 1
    d6 = randint(0, 5) + 1
    d7 = randint(0, 5) + 1
    d8 = randint(0, 5) + 1
    if d1 + d3 + d5 + d7 == 12 and d2 + d4 + d6 + d8 == 11 and d2 * d3 * d7 == 24 and d1 * d2 * d3 * d5 == 60 and d7 - d2 + d3 - d4 == 0 and d6 + d1 + d8 == 10 and d8 > 3:
        flag = f"fiap{{{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}}}"
        print(flag)