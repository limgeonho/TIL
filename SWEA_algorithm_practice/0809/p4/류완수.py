import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 각 testcase를 cards 리스트로 반환
    cards = list(map(int, input()))

    # 변수 초기화, 정렬
    run = 0
    triplet = 0
    cards.sort()

    for card in cards:
        # triplet이 나오는 경우를 찾아 triplet에 1 추가, triplet 만든 카드 쌍 제거
        if cards.count(card) >= 3:
            triplet += 1
            for _ in range(3):
                cards.remove(card)
    # 남은 카드들 중에서
    for card in cards:
        # run 만드는 경우 찾아 run에 1 추가, run 만든 카드 3장 제거
        if card + 1 in cards and card + 2 in cards:
            cards.remove(card)
            cards.remove(card + 1)
            cards.remove(card + 2)
            run += 1
    # 남은 카드 중에서 run 만드는 경우 찾아 run에 1 추가
    for card in cards:
        if card + 1 == cards[1] and card + 2 == cards[2]:
            run += 1
    # run과 triplet로만 이루어진 경우(합이 2인 경우) return True
    if triplet + run == 2:
        print(True)
    else:
        print(False)
