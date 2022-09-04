import sys
from collections import deque

di = [0,-1,0,1]
dj = [-1,0,1,0]

def bfs(M,N):
    global box
    global que
    while que:
        tmp = que.popleft()
        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == 0:
                box[ni][nj] = box[tmp[0]][tmp[1]] + 1
                que.append((ni, nj))


M, N = map(int, sys.stdin.readline().split())

box = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ans = 0
que = deque([])
tomato = False

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            que.append((i,j))
        elif box[i][j] == 0:
            tomato = True

if not tomato:
    print(0)
else:
    bfs(M, N)
    flag = True
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                ans = 0
                flag = False
                break
            else:
                if ans < box[i][j]:
                    ans = box[i][j]

        if not flag:
            break

    print(ans-1)

