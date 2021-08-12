import sys
import itertools
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    array_a = list(range(1, 13))
    cnt = 0
    N, K = map(int, input().split())
    subsets = list(itertools.combinations(array_a, N))
    for subset in subsets:
        if sum(subset) == K:
            cnt += 1
    print(f'#{tc} {cnt}')
