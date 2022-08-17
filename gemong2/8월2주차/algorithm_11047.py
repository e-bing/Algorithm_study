N, K = map(int, input().split())
cnt = 0
Ai = [int(input()) for _ in range(N)]

for j in Ai[::-1]:
    if K == 0:
        break
    if j < K:
        cnt += K // j
        K = K % j


print(cnt)