import sys
sys.stdin = open('input.txt')

# N, M = map(int, input().split())
#
# matrix = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# matrix

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(matrix)
