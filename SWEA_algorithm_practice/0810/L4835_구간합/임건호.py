import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    tmp = []
    # 원하는 구간 만큼 리스트를 자르고 리스트의 합을 임의 tmp리스트에 append
    for i in range(n-m+1):
        tmp.append(sum(nums[i: i+m]))

    # tmp에는 구간별로 잘린 리스트들의 합이 들어가 있기 때문에 이 중 가장 큰 값에서 작은 값을 빼면 된다.
    print(f'#{tc} {max(tmp) - min(tmp)}')

