import sys
sys.stdin = open('input.txt')

a = int(input())
numbers = list(map(int, input().split()))

for _ in range(int(input())):
    print(input())
