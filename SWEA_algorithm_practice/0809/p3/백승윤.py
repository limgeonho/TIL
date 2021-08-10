# solved by YoonBaek

import sys

def get_inception_room(row: int, col: int, box_heights: list)->list:
    """
    returns rotated room structure.
    """
    room = [[0] * col for _ in range(row)]

    for r in range(row):
        for c in range(box_heights[r]):
            room[r][c] = 1

    return room


if __name__ == "__main__":
    sys.stdin = open("input.txt")

    tc = int(input())

    for _ in range(tc):
        row = int(input())
        box_heights = list(map(int, input().split()))
        col = max(box_heights)

        room = get_inception_room(row, col, box_heights)

        max_fall = 0

        for c in range(col):
            # if box starts, counting begins
            box_start = False
            fall_cnt = 0

            for r in range(row):
                if room[r][c]:
                    box_start = True
                else :
                    if box_start:
                        fall_cnt += 1

            max_fall = fall_cnt if fall_cnt > max_fall else max_fall

        print(max_fall)