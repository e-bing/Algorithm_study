from collections import deque

N, M, K = map(int, input().split())

arr = deque([list(map(int, input().split())) for _ in range(M)])


# 각기 현재 인덱스, 0~7번 이동방향 지정
# 굳이 현재 인덱스 번호까지 넣은 이유는 파이썬 규칙을 따르기 위함임
route = {
    "0" : [-1, 0],
    "1" : [-1, 1],
    "2" : [0, 1],
    "3" : [1, 1],
    "4" : [1, 0],
    "5" : [1, -1],
    "6" : [0, -1],
    "7" : [-1, -1],
}
di = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 0, 1, 1, 1, 0, -1, -1, -1]

for k in range(K):
    space = [[list() for _ in range(N + 1)] for _ in range(N + 1)]

    while arr:    
        a = arr.popleft()
        if a[2] == 0:
            pass
        else:
            gothere = route[str(a[4])]

            i, j = a[0] + (gothere[0] * a[3]) , a[1] + (gothere[1] * a[3])
            print(i, j)
            if N < i:
                i = i % N
            elif i == 0:
                i = N
            elif i < 0:
                i += N
            if N < j:
                j = j % N
            elif j == 0:
                j = N
            elif j < 0:
                j += N

            print(i, j)
            space[i][j].append([a[2], a[3], a[4]])


    for x in range(N + 1):
        for y in range(N + 1):
            print(x, y)
            fireballs = space[x][y]
            if len(fireballs) == 0:
                pass
            elif len(fireballs) == 1:
                arr.append([x, y, fireballs[0][0], fireballs[0][1], fireballs[0][2]])
            else:
                mass = 0
                speed = 0
                check = 0
                reroute = [1, 3, 5, 7]
                for fireball in fireballs:
                    mass += fireball[0]
                    speed += fireball[1]
                    check += (fireball[2] % 2)

                mass, speed = (mass // 5), (speed // len(fireballs))

                if check == 0 or check == len(fireballs):
                    reroute = [0, 2, 4, 6]
                
                for i in range(4):
                    arr.append([x, y, mass, speed, reroute[i]])
    

total = 0
for a in arr:
    total += a[2]

print(total)