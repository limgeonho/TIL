import sys

sys.stdin = open("input.txt")

N, M = map(int, input().split())

list2d = []

for _ in range(N):
    list2d.append(input().split())

print(list2d)
