import sys
sys.stdin = open("input.txt")

for test in range(1, int(input())+1):
    column_cnt = int(input())
    boxes = list(map(int, input().split()))
    heights = []
    for col_num in range(column_cnt):
        bottom_cnt = 0
        for j in range(col_num,column_cnt):
            if boxes[col_num] <= boxes[j]:
                bottom_cnt += 1
        heights.append(column_cnt-col_num-bottom_cnt)
    print(max(heights))
