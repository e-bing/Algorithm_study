import sys
from collections import deque

def bfs(start_i,start_j,state,N,M):
    global visited
    que = deque()
    que.append((start_i,start_j,state))
    visited[start_i][start_j][state] = 1

    while que:
        tmp = que.popleft()
        if tmp[0] == N-1 and tmp[1] == M-1:
            # print(visited)
            return visited[tmp[0]][tmp[1]][tmp[2]]
        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj][tmp[2]] == 0:
                que.append((ni,nj,tmp[2]))
                visited[ni][nj][tmp[2]] = visited[tmp[0]][tmp[1]][tmp[2]] + 1
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and tmp[2] == 0:
                que.append((ni,nj,tmp[2]+1))
                visited[ni][nj][tmp[2]+1] = visited[tmp[0]][tmp[1]][tmp[2]] + 1

    # print(visited)
    return -1


N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]


print(bfs(0,0,0,N,M))