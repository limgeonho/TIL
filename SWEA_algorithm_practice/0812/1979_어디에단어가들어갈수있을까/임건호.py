import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N):
        possible = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                possible += 1
            if puzzle[i][j] == 0 or j == N-1:
                if possible == K:
                    cnt += 1
                possible = 0

        for j in range(N):
            if puzzle[j][i] == 1:
                possible += 1
            if puzzle[j][i] == 0 or j == N - 1:
                if possible == K:
                    cnt += 1
                possible = 0

    print(f'#{tc} {cnt}')