import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    board = [[0] * 10 for _ in range(10)]
    purple = 0
    N = int(input())
    for _ in range(N):
        color_info = list(map(int, input().split()))
        for i in range(color_info[0], color_info[2] + 1):
            for j in range(color_info[1], color_info[3] + 1):
                board[i][j] += color_info[4]

    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                purple += 1
    print(f'#{tc} {purple}')
