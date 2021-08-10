import sys


sys.stdin = open('input.txt')
T = int(input())


for i in range(1, T+1):

    # 가로 길이는 주어진 상자 높이의 개수만큼으로 설정합니다.
    N = int(input())
    box_height = list(map(int, input().split()))

    # 세로 길이는 최대 높이로 설정합니다.
    M = max(box_height)
    box_array = [[0]*(M+1) for _ in range(N)]

    # 빈 box_array 를 box_height 에 맞춰 채웁니다.
    for i in range(N):
        for j in range(box_height[i]):
            box_array[i][j] = 1

    # fall 에는, 쌓아져있는 상자 중에 가장 위에 위치한 상자의 낙하 거리를 저장합니다.
    fall = []
    for i in range(N):
        now_height = box_height[i]-1
        if box_array[i][now_height]:
            below = 0

            # 오른쪽으로 한칸씩 이동하면서, 지금 선택한 상자의 아래에 몇개의 상자가 있는지 셉니다.
            for j in range(i+1, N):
                if box_array[j][now_height]:
                    below += 1

            # 낙하 거리를 구합니다.
            fall.append(N-1 - i - below)

    print(max(fall))






