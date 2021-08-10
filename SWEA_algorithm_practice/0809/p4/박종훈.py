import sys
from itertools import combinations  # 조합 기능을 사용하기 위해 모듈 불러오기

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    cards = list(map(int, list(input())))
    cases = list(combinations(cards, 3))  # 6C3
    for i in range(len(cases)//2):  # 0~9
        case1, case2 = list(cases[i]), list(cases[len(cases) - (i+1)])
        c1 = c2 = False
        # triplet, run 판별
        if case1.count(case1[0]) == 3:
            c1 = True
        else:
            case1.sort()
            if case1[0]+1 == case1[1] and case1[1]+1 == case1[2]:
                c1 = True
        if case2.count(case2[0]) == 3:
            c2 = True
        else:
            case2.sort()
            if case2[0] + 1 == case2[1] and case2[1] + 1 == case2[2]:
                c2 = True
        # baby gin이면 True 출력
        if c1 == True and c2 == True:
            print(True)
            break
    # for문이 끝날 때까지 True가 아니라면 False 출력
    else:
        print(False)
