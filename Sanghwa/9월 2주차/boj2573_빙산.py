from collections import deque

def bfs(check, count, si, sj):
    que = deque()
    que.append((si,sj))
    check[si][sj] = 1
    while que:
        tmp = que.popleft()
        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if board[ni][nj] != 0 and check[ni][nj] == 0:
                que.append((ni, nj))
                check[ni][nj] = 1
            elif board[ni][nj] == 0:
                count[tmp[0]][tmp[1]] += 1


N, M = map(int, input().split())

board = list(list(map(int,input().split())) for _ in range(N))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

year = 0

while True:
    ice_cnt = 0
    check = [[0] * M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and check[i][j] == 0:
                bfs(check, count, i, j)
                ice_cnt += 1

    for i in range(N):
        for j in range(M):
            board[i][j] -= count[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    if ice_cnt == 0:
        print(0)
        break
    if ice_cnt >= 2:
        print(year)
        break

    year += 1