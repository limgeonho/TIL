import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    answer = []
    array.sort(reverse=True)

    for i in range(N//2):
        answer.append(array[i])
        answer.append(array[-(i+1)])

    print(f'#{tc}', end=' ')
    print(*answer[:10])
