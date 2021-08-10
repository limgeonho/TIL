import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    cnt = int(input())
    boxes = list(map(int, input().split()))

    # 평탄화를 하기 위해 처음에 높이 순서대로 정렬 => 처음과 마지막에서 +1, -1을 해줌 => 또 정렬... 반복
    for _ in range(cnt):
        boxes.sort()
        boxes[-1] -= 1
        boxes[0] += 1
    print(f'#{tc} {max(boxes) - min(boxes)}')
