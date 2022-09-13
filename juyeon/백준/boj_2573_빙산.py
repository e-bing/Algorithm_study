# def dfs(arr, v):
    
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(N)]

turn = 1
division = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while True:
    sum_iceberg = 0
    total = 0
    for x in range(N):
        for y in range(M):
            if iceberg[x][y] > 0:
                total += 1
                sum_iceberg += iceberg[x][y]

    # 만약 빙하가 모두 녹았다면, turn을 0으로 재설정한 후, break
    if sum_iceberg == 0:
        turn = 0
        break
    # 만약 위의 두 탈출 조건 중 어느 쪽에도 해당되지 않는다면, 델타탐색 및 bfs 실행
    else:
        turn += 1
        visited_list = [[0] * M for _ in range(N)]
        true = 0

        for x in range(N):
            for y in range(M):
                if visited_list[x][y] == 0:
                    queue = deque([(x, y)])
                    visited_list[x][y] = 1

                # print(queue)
                search = [(x, y)]
                while queue:
                    # print(queue)
                    i, j = queue.pop()
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 1 <= ni < (N - 1) and 1 <= nj < (M - 1) and visited_list[ni][nj] == 0:
                            if iceberg[ni][nj] > 0:
                                queue.appendleft((ni, nj))
                                visited_list[ni][nj] = 1
                                search.append((ni, nj))
                # print(search)
                if len(search) == total:
                    pass
                else:
                    division = 1
                    break
    # 민약 분리가 일어났다면, break
    if division == 1:
        break


print(turn)             

