import sys
sys.stdin = open('input.txt')

def babygin(numbers):
    count = [0] * 10
    i = 0
    run, triplet = 0, 0

    for number in numbers:
        count[number] += 1

    while i < 10:
        if count[i] >= 3:
            count[i] -= 3
            triplet += 1
            continue

        if count[i]>0 and count[i+1]>0 and count[i+2]>0:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            run += 1
            continue

        else:
            i += 1

    if (run + triplet) == 2:
        return True
    else:
        return False

T = int(input())

for tc in range(1, T+1):

    cards = list(map(int, list(input())))
    print(babygin(cards))
