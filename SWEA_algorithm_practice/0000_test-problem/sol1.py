import sys
# 파일에 있는 내용을 input함수에 연결 + 엔터 단위로 끊어서 들어옴
sys.stdin = open('input.txt')

# var = input()

# 문자열로 들어온다
# print(var == '7 8')

# 한 번에 사용
N, M = map(int, input().split())

numbers = list(map(int, input().split()))

print(N, M, numbers)