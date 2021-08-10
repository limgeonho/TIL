import sys

sys.stdin = open("input.txt")

for _ in range(int(input())):
    N = int(input())
    box = list(map(int, input().split()))

    # 낙차를 기록한 변수를 생성합니다.
    fall = 0
    for i in range(len(box)) :
        # 90도 돌려졌을 때 아래에 있을 박스들을 카운트 할 변수를 생성합니다.
        count = 0
        for j in range(i+1, len(box)):
            # 어차피 해당 행의 최고 높이에 있는 상자만 비교해 주면 됩니다.
            if box[i] <= box[j]:
                #  i행의 최고 높이 박스가 90도 돌려졌을 때 아래에 있을 박스들을 카운트해줍니다.
                count+=1
        # 이전에 기록한 낙차보다 현재 상자의 낙차가 크다면 바꿔줍니다.
        if fall < N-i-1-count:
            fall = N-i-1-count

        # 더 이상 탐색할 이유가 없다면 탐색 멈춥니다.
        if fall >= N-i:
            break
    print(fall)

