import sys
sys.stdin = open('input.txt')

def Gravity(box):
    n = len(box)
    count = [0]*n
    max_fall_count = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            if box[j] >= box[i]:
                count[i] += 1

    for i in range(0, n):
        if (n - (i+1) - count[i]) > max_fall_count:
            max_fall_count = n - (i+1) - count[i]
            max_fall_box = i+1

    return max_fall_box, max_fall_count

T = int(input())

for _ in range(T):
    N = input()
    box_list = list(map(int, list(input().split())))
    print(Gravity(box_list))
