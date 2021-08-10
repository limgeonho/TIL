import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    fuel, destination, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    bus_pos = 0
    cnt = 0
    lane = [0] * destination

    for charger in chargers:
        lane[charger] = 1

    while True:
        bus_pos += fuel
        if bus_pos >= destination:
            break
        if lane[bus_pos] == 0:
            for i in range(bus_pos, bus_pos-fuel, -1):
                if lane[i] == 1:
                    bus_pos = i
                    cnt += 1
                    break
            else:
                cnt = 0
                break
        else:
            cnt += 1

    print(f'#{tc} {cnt}')
