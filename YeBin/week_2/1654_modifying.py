# BaekJoon 1654 랜선 자르기
# 2022-08-14

K, N = map(int, input().split())
lan = []
for i in range(K):
    lan.append(int(input()))
start = 0
end = sum(lan) // N
cnt = 0
mid = (start + end) // 2 + 1
while (start < end - 1):
    mid = (start + end) // 2 + 1
    if mid == 0:
        mid = 1
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt < N:
        end = mid
    elif cnt >= N:
        start = mid

print(mid)

