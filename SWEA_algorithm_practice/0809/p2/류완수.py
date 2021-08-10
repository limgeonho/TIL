import sys
sys.stdin = open('input.txt')

"""
[
    [0 1 2 3]
    [4 5 6 7]
    [8 9 10 11]
]
"""

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
matrix