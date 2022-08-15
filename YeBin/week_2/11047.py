# BaekJoon 11047 동전 0
# 2022-08-14

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

idx = 0
for i in range(1, N):
    if K >= coins[-i]:
        idx = N - i
        break

cnt = 0
while (idx >= 0) and (K > 0):
    cnt += K // coins[idx]
    K %= coins[idx]
    idx -= 1

print(cnt)