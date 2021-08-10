# solved by YoonBaek
import sys

def inputs()-> list:
    return list(map(int, input()))

def counting_sort(cards: list)-> list:
    counts = [0] * 10

    for card in cards:
        counts[card] += 1

    return counts

def is_triplete(cards: list) -> int:
    cnt = 0
    for i in range(10):
        cnt += cards[i] // 3
        cards[i] -= cnt*3
    return cnt

def is_run(cards: list) -> int:
    cnt, check_seq = 0, 0
    for i in range(7):
        point = cards[i]
        if point:
            if point == cards[i+1] == cards[i+2]:
                cnt += point
                cards[i] -= point
                cards[i+1] -= point
                cards[i+2] -= point

    return cnt


if __name__ == "__main__":
    sys.stdin = open("input.txt")

    tc = int(input())

    for _ in range(tc):
        cards = inputs()

        sorted_cards = counting_sort(cards)

        if is_run(sorted_cards) + is_triplete(sorted_cards) >= 2:
            print("Baby Gin")
        else :
            print("Lose")
