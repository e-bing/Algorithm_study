C = int(input())
N = int(input())
arr = [[] for _ in range(C + 1)]

for i in range(N):
    ai, aj = map(int, input().split())
    arr[ai].append(aj)
    arr[aj].append(ai)


def dfs(j):
    visited = [False for _ in range(N)]
    visited[j] = True
    print(j, end=' ')
    for k in arr[j]:
        if visited == False:
            dfs(k)


dfs(1)
