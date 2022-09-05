# BaekJoon 18310 안테나
# 2022-09-04

N = int(input())
houses = list(map(int, input().split()))

houses.sort()
print(houses[(N-1) // 2])