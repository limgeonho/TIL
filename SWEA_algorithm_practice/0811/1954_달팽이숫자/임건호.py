import sys
sys.stdin = open('input.txt')

T = int(input())

# 우 하 좌 상 => 이게 제일 중요한듯..!
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    x = y = direction = 0

    for number in range(1, N*N+1):
        snail[x][y] = number
        x += dx[direction]
        y += dy[direction]
        # 아래의 조건을 충족하면 방향 전환(나가거나 앞에 다른 수가 있을때)
        if x < 0 or x >= N or y < 0 or y >= N or snail[x][y] != 0:
            # 일단 잘못 간 한 번을 뒤로 되돌리기
            x -= dx[direction]
            y -= dy[direction]
            # 방향 전환(빙글빙글)
            direction = (direction+1) % 4
            # 바뀐 방향으로 진행
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    for num in snail:
        print(*num)


