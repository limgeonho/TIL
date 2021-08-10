import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, q = map(int, input().split())
    board = [0] * n

    # l과 r을 입력받고 2중 for문 중 첫 번째 for문 순서 값을 해당하는 board의 값에 대입한다.
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            board[j] = i+1

    # 결과 리스트안에 있는 int를 전부 str로 변환하고 이를 join을 통해서 전체 str로 반환한다.
    result = ' '.join(map(str, board))
    print(f'#{tc} {result}')
