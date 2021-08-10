import sys
sys.stdin = open('input.txt')


def is_baby_gin(cards):
    run = 0
    tri = 0

    counters = [0]*10
    for card in cards:
        counters[card] += 1

    idx = 0
    while idx < 10:
        if counters[idx] >= 3:
            tri += 1
            counters[idx] -= 3
            continue

        if idx < 8 and counters[idx] and counters[idx+1] and counters[idx+2]:
            run += 1
            counters[idx] -= 1
            counters[idx+1] -= 1
            counters[idx+2] -= 1
            continue

        idx += 1

    if run + tri == 2:
        return True
    else:
        return False


T = int(input())

for _ in range(T):
    cards = [int(c) for c in input()]
    if is_baby_gin(cards):
        print('Baby-gin!')
    else:
        print('Nope')
