import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))

    max_cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if blocks[i] > blocks[j]:
                cnt += 1
        max_cnt = cnt if max_cnt < cnt else max_cnt

    print(max_cnt)
