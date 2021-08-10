import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    M = int(input())
    boxes = list(map(int, input().split()))
    max_num = boxes[0]
    cnt = 0
    max_list = []
    cnt_list = []

    for i in range(M):
        cnt += 1
        if max_num <= boxes[i]:
            max_list.append(max_num)
            cnt_list.append(cnt)
            max_num = boxes[i]
            cnt = 0

    max_list.append(max_num)
    cnt_list.append(cnt)
    max_num = 0
    cnt = 0

    for i in range(len(cnt_list)):
        if cnt < cnt_list[i]:
            cnt = cnt_list[i]

    print(cnt)
