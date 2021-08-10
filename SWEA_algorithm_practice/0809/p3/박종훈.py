import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):

    N = int(input())
    boxes = list(map(int, input().split()))
    result = 0

    for i in range(N-1):
        cnt = 0
        # 왼쪽부터 한 칸씩 오른쪽으로 가면서 뒤에 있는 박스의 높이가 더 낮다면 cnt += 1
        for box in boxes[i+1:]:
            if boxes[i] > box:
                cnt += 1
        # result 갱신
        if cnt > result:
            result = cnt
    # 결과 출력
    print(result)
