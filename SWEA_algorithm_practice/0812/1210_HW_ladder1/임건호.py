import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]

    x, y = 99, board[99].index(2)
    visited[x][y] = 1

    while True:
        if x == 0:
            destination = y
            break
        else:

            if y-1 >= 0 and board[x][y-1] == 1 and visited[x][y-1] == 0:
                visited[x][y-1] = 1
                y -= 1

                continue

            elif y+1 < 100 and board[x][y+1] == 1 and visited[x][y+1] == 0:
                visited[x][y+1] = 1
                y += 1

                continue
            else:
                visited[x-1][y] = 1
                x -= 1

    print(f'#{T} {destination}')

