import sys
sys.stdin = open('input.txt')

for num in range(int(input())):
    result = [0] * 10
    run = 0
    triplet = 0
    i = 0

    for num in list(map(int, list(input()))):
        result[num] += 1

    while i < 10:
        if result[i] >= 3:
            triplet += 1
            result[i] -= 3
            if triplet == 2:
                print('baby-gin')
                continue

        else:
            while i < 8:
                if result[i] >= 1 and result[i+1] >= 1 and result[i+2] >= 1:
                    run += 1
                    result[i] -= 1
                    result[i + 1] -= 1
                    result[i + 2] -= 1
                    if (run == 1 and triplet) == 1 or run ==2:
                        print('baby-gin')
                        continue
                else:
                    break
            i += 1
