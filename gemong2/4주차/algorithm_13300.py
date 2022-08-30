N, K = map(int, input().split())
m = [0] *6
w = [0] *6
room = 0

for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        w[Y-1] += 1
    else:
        m[Y-1] += 1

for j in range(6):
    if w[j] == 0:
        pass
    elif w[j] % K == 0:
        room += (w[j] // K )
        w[j] = 0
    else:
        if w[j] // K > 0:
            room += ((w[j] // K) + 1 )
            w[j] = 0
        else:
            room += 1
            w[j] = 0


    if m[j] == 0:
        pass
    elif m[j] % K == 0:
        room += (m[j] // K )
        m[j] = 0
    else:
        if m[j] // K > 0:
            room += ((m[j] // K) + 1 )
            m[j] = 0
        else:
            room += 1
            m[j] = 0

print(room)