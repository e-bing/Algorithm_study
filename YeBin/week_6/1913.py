# BaekJoon 1913 달팽이
# 2022-09-12

import sys
sys.stdin = open('1913_input.txt', 'r')

N = int(input())
target = int(input())
coord = [-1, -1]
data = [[0] * N for i in range(N)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cur = [N // 2, N // 2]
M = 0
dir_idx = -1
num = 1
data[cur[0]][cur[1]] = num
if num == target:
    coord[0] = cur[0] + 1
    coord[1] = cur[1] + 1
for i in range(N * 2 - 1):
    dir_idx = (dir_idx + 1) % 4
    if (i % 2 == 0) and (i < (N - 1) * 2):
        M += 1
    for j in range(M):
        num += 1
        cur[0] += direction[dir_idx][0]
        cur[1] += direction[dir_idx][1]
        data[cur[0]][cur[1]] = num
        if num == target:
            coord[0] = cur[0] + 1
            coord[1] = cur[1] + 1

for i in data:
    print(*i)
print(coord[0], coord[1])
