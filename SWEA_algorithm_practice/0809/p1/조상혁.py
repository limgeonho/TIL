import sys

sys.stdin = open('input.txt')

a = int(input())
numbers = list(map(int, input().split()))

n = int(input())

for _ in range(n):
    print(input())
