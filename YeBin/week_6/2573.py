# BaekJoon 2573 빙산
# 2022-09-12

import sys
sys.stdin = open('2573_input.txt', 'r')

import collections


def bfs(a, b):
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            n_x = x + direction[i][0]
            n_y = y + direction[i][1]
            if ice[n_x][n_y] > 0 and visited[n_x][n_y] == 0:
                visited[n_x][n_y] = 1
                queue.append((n_x, n_y))
    return 1


N, M = map(int, input().split())
ice = [list(map(int, input().split())) for i in range(N)]
temp = [[0 for i in range(M)] for i in range(N)]

ice_num = 1
year = 0
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
queue = collections.deque()
cnt = 0
while ice_num:
    ice_num = 0
    result = 0
    visited = [[0] * M for i in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            cnt = 0
            if ice[i][j] > 0:
                ice_num += 1
                for k in range(4):
                    if ice[i + direction[k][0]][j + direction[k][1]] == 0:
                        cnt += 1
                if ice[i][j] - cnt > 0:
                    temp[i][j] = ice[i][j] - cnt
                else:
                    temp[i][j] = 0
    if ice_num == 0:
        year = 0
        break

    for i in range(1, N-1):
        for j in range(1, M-1):
            if ice[i][j] > 0 and visited[i][j] == 0:
                result += bfs(i, j)
    if result > 1:
        break
    year += 1
    ice = temp
    temp = [[0 for j in range(M)] for i in range(N)]
print(year)
