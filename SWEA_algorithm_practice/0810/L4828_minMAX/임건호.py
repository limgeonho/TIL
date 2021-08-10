import sys
sys.stdin = open('input.txt')

T = int(input())

# 리스트를 입력받고 그냥 최대, 최소 구하기
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    print(f'#{tc} {max(nums) - min(nums)}')
