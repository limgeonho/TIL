import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(arr)