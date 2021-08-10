import sys
sys.stdin = open('input.txt')


def is_baby_gin(num_cnt):
    run, triplet = 0, 0

    for idx, cnt in enumerate(num_cnt):
        if cnt >= 6 or num_cnt[idx:idx+3] == [2, 2, 2]:
            return True
        if cnt >= 3:
            triplet += 1
            num_cnt[idx] -= 3
        if num_cnt[idx:idx+3] == [1, 1, 1]:
            run += 1
    return True if triplet + run == 2 else False


for _ in range(int(input())):
    numbers = list(map(int, input()))
    cnt_list = [0]*10

    for number in numbers:
        cnt_list[number] += 1

    print(is_baby_gin(cnt_list))
