import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    boxes = list(map(int, input().split()))

    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if boxes[i] <= boxes[j]:
                cnt = cnt + 1
        answer = max(answer, N-i-cnt-1)
    print(answer)
