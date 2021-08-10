import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    diff = 0
    end = True
    for i in range(N):
        for j in range(i+1, N):
            if arr[j] >= arr[i]:
                end = False
                if diff < j - i:
                    diff = j - i
                    break

        if end and diff < N - i:
            diff = N - i
        end = True
    
    print(diff)