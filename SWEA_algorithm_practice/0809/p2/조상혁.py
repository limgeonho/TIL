import sys

sys.stdin = open("input.txt")

row, col = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(row)]


print(matrix)