N, K = map(int,input().split())

coins = []
cnt = 0

for i in range(N):
    coins.append(int(input()))

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        cnt += K//coins[i]
        K -= ((K//coins[i])*coins[i])

print(cnt)
