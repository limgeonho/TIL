# import sys
#
# sys.stdin = open('input.txt')


# 정수 리스트에서 최대값을 반환해주는 함수
def get_max(numbers):
    max_num = 0
    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num


def get_cumulative_counts(numbers):
    # get a maximum number in the list
    k = get_max(numbers)

    # declare a list for counting
    counts = [0 for _ in range(k+1)]

    for number in numbers:
        counts[number] += 1

    # cumulate the counts
    for i in range(k):
        counts[i+1] += counts[i]

    return counts


def is_baby_gin(numbers):
    i = 0
    k = get_max(numbers)
    counts = get_cumulative_counts(numbers)

    # 순회하면서 triplet 존재하면 제거해준다
    while i <= k:
        if counts[i] >= 3:
            counts[i] -= 3
        else:
            i += 1

    i = 0

    # run 이 존재하는지 판별하고 존재한다면 제거
    while i < k-1:
        # run 이 존재하면 제거해준다.
        if counts[i] * counts[i+1] * counts[i+2]:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
        else:
            i += 1

    return True if counts == [0 for _ in range(k+1)] else False


if __name__ == '__main__':
    # N = int(input())
    # for _ in range(N):
    numbers = list(map(int, input()))
    print(is_baby_gin(numbers))
