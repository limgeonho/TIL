import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(input(()))

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    sum_num = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < n:
                    tmp = abs(board[ni][nj] - board[i][j])
                    sum_num += tmp
    print(f'#{tc} {sum_num}')
