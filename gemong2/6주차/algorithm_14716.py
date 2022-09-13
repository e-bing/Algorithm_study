import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):

    if i <= -1 or i >= M or j <= -1 or j >= N:
        return False

    if arr[i][j] == 1:

        arr[i][j] = 0
        dfs(i + 1, j)
        dfs(i + 1, j + 1)
        dfs(i + 1, j - 1)
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i - 1, j)
        dfs(i - 1, j + 1)
        dfs(i - 1, j - 1)

        return True
    return False


M, N = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(M)]

cnt = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)
