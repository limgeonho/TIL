import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    numbers = int(input())
    counts = [0] * 10

    for n in numbers:
        counts[n % 10] += 1
        numbers //= 10

    i = 0
    tri = run = 0

    while i < 10:
        if counts[i] >= 3:
            counts[i] -= 3
            tri += 1
            continue
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2:
        print('baby-gin')
    else:
        print('not baby-gin')        
