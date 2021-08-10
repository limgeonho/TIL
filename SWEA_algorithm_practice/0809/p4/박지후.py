import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    num = [int(_) for _ in input()]

    not_baby_gin = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

    baby_gin = True
    if sum(num) % 3:
        baby_gin = False
    for case in not_baby_gin:
        if case[0] in num and case[1] in num and case[2] in num:
            baby_gin = False
            break
    if baby_gin:
        print("Baby-gin")
    else:
        print("Not Baby-gin")











