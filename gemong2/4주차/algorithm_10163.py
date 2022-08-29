#직사각형의 개수
N = int(input())
arr = [[0]*1001 for _ in range(1001)]

for k in range(1,N+1):
    M = list(map(int, input().split()))
    i = M[0]
    j = M[1]
    arr[i][j] = k
    for p in range(i,i+M[2]):
        for q in range(j,j+M[3]):
            if p < 1001 and q <1001:
                arr[p][q] = k
idx = 1

while idx <= N:
    cnt = 0
    for u in range(1001):
        for y in range(1001):
            if arr[u][y] == idx:
                cnt += 1
    if cnt == 0:
        print(0)
    else:    
        print(cnt)
    idx += 1