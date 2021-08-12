import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    bug_group = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            bugs = 0
            for k in range(M):
                for l in range(M):
                    bugs += board[i+k][j+l]
            bug_group.append(bugs)
    print(f'#{tc} {max(bug_group)}')