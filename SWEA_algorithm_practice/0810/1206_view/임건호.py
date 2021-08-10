import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    apartments = list(map(int, input().split()))
    result = 0

    for i in range(2, T-2):
        if apartments[i-2] > apartments[i] or apartments[i-1] > apartments[i]:
            continue
        elif apartments[i+2] > apartments[i] or apartments[i+1] > apartments[i]:
            continue
        else:
            left_tmp = 0
            right_tmp = 0
            final = 0

            left_tmp = apartments[i] - apartments[i-1]
            right_tmp = apartments[i] - apartments[i+1]
            final_one = min(left_tmp, right_tmp)
            left_tmp = apartments[i] - apartments[i-2]
            right_tmp = apartments[i] - apartments[i+2]
            final_two = min(left_tmp, right_tmp)
            final = min(final_one, final_two)

            result += final
    print(f'#{tc} {result}')
