N, H, T = map(int, input().split())
giant = []
cnt = 0
for i in range(N):
    tmp = int(input())
    giant.append(tmp)

for k in range(T):
    if max(giant) < H or max(giant) == 1:
        break
    else:
        for j in range(N):
            if giant[j] == max(giant):
                giant[j] = giant[j] // 2
                cnt += 1


if max(giant) >= H:
    print('NO')
    print(max(giant))
else:
    print('YES')
    print(cnt)
