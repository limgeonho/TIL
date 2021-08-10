import sys
sys.stdin = open('input.txt')


def maximum_drop(heights):
    maximum = 0
    for idx, height in enumerate(heights):
        cnt = 0
        # 오른쪽 상자들 중 지금보다 더 높은 상자들 개수 세기
        for nxt in heights[idx+1:]:
            if nxt < height:
                cnt += 1

        if maximum < cnt:
            maximum = cnt

    return maximum


T = int(input())

for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    print(maximum_drop(heights))
