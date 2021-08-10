import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = input()
    check = [0] * n
    tmp = []

    # 각각의 숫자가 몇 번씩 나오는지 count()
    for i in range(n):
        check[i] = nums.count(nums[i])

    # 그 중 가장 카운팅이 큰 수를 찾는다.
    max_cnt = max(check)

    # 카운팅이 가장 큰 수와 같은 인덱스에 위치하는 수를 누적한다.
    for i in range(n):
        if max_cnt == check[i]:
            tmp.append(nums[i])

    # 여러번 등장 할 수도 있기 때문에 그 중 가장 큰 수를 찾는다.
    max_num = max(tmp)

    print(f'#{tc} {max_num} {max_cnt}')
