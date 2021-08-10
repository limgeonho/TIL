import sys
from collections import Counter

sys.stdin = open("input.txt")

N = int(input())

inputs = [input() for _ in range(N)]

for input in inputs:
    # 카운터로 숫자의 개수를 세어줍니다.
    dict =Counter([ int(s) for s in input])

    baby_gin = 0
    # 입력된 각 숫자에 대해 탐색합니다.
    for key in dict.keys():
        # 만약 해당 숫자에서 baby-gin 요소가 있었다면, 해당 숫자에 대해 다시 한번 탐색해줍니다.
        # 333333 이나 112233 와 같이 한 숫자에서 baby-gin이 중첩되어 나타나는 경우를 찾기 위함입니다.
        again = True
        while (again):
            again = False
            # 한 숫자의 개수가 3개 이상이면 baby-gin 카운트를 올리고, 개수에 3을 빼줘서 이후 카운트에서 제외 합니다.
            if dict[key] >=3:
                dict[key] -=3
                baby_gin +=1
                again = True

            # 연속된 숫자가 존재한다면 baby-gin 카운트를 올리고, 각각의 개수를 1씩 빼줘 이후 카운트에서 제외합니다.
            if dict.get(key, -1) > 0 and dict.get(key+1, -1) > 0 and dict.get(key+2, -1) > 0 :
                dict[key] -= 1
                dict[key+1] -= 1
                dict[key+2] -= 1
                baby_gin += 1
                again = True
    print(baby_gin==2)

