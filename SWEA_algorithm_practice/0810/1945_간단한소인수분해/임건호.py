import sys
sys.stdin = open('input.txt')

T = int(input())
# 이건 뭐 그냥... 하나씩 나눠보고 해당되면 누적하고 반복
for tc in range(1, T+1):
    n = int(input())
    a = b = c = d = e = 0
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            a += 1
            n //= 2
        if n % 3 == 0:
            b += 1
            n //= 3
        if n % 5 == 0:
            c += 1
            n //= 5
        if n % 7 == 0:
            d += 1
            n //= 7
        if n % 11 == 0:
            e += 1
            n //= 11
    print(f'#{tc} {a} {b} {c} {d} {e}')


