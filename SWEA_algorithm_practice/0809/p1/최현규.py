import sys
sys.stdin = open('input.txt')

a = int(input())
numbers = list(map(int, input().split()))

N = int(input())

for _ in range(N):
    print(input())