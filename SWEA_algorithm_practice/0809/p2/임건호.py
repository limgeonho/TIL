import sys

sys.stdin = open('input.txt')

m, n = map(int, input().split())

board = [list(map(int, input().split()))for _ in range(m)]

print(board)