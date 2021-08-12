import sys
sys.stdin = open('input.txt')


def binary_search(pages, target, start, end):
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if pages[mid] == target:
            return cnt
        elif pages[mid] < target:
            start = mid
            cnt += 1
        else:
            end = mid
            cnt += 1


T = int(input())
for tc in range(1, T+1):
    page, a, b = map(int, input().split())

    pages = list(range(1, page+1))
    cnt_a = binary_search(pages, a, 0, len(pages)-1)
    cnt_b = binary_search(pages, b, 0, len(pages)-1)

    if cnt_a > cnt_b:
        answer = 'B'
    elif cnt_a == cnt_b:
        answer = 0
    else:
        answer = 'A'

    print(f'#{tc} {answer}')
