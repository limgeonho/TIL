import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))

    array.sort()

    print(f'#{tc}', end=' ')
    print(*array)