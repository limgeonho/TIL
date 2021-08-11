import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    tmp_row = 0
    tmp_col = 0
    tmp_cross_right = 0
    tmp_cross_reverse = 0

    board = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        tmp_row = max(tmp_row, sum(board[i]))

    for i in range(100):
        total = 0
        for j in range(100):
            total += board[j][i]
        tmp_col = max(tmp_col, total)

    for i in range(100):
        for j in range(100):
            if i + j == 99:
                tmp_cross_right += board[i][j]

    for i in range(100):
        for j in range(100):
            if i == j:
                tmp_cross_reverse += board[i][j]

    print(f'#{T} {max(tmp_row, tmp_col, tmp_cross_right, tmp_cross_reverse)}')