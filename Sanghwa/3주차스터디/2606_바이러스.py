import sys
from collections import deque

def bfs(start, step, N):
    visited = [0]*(N+1)
    que = deque([])
    que.append(start)
    while que:
        tmp = que.popleft()
        if visited[tmp] == 0:
            visited[tmp] = step
            step += 1
            for i in edge[tmp]:
                if i !=0 and visited[i] == 0:
                    que.append(i)

    # print(visited)
    return max(visited)


computer = int(sys.stdin.readline())

num_edge = int(sys.stdin.readline())

edge = [[] for _ in range(computer+1)]

for i in range(num_edge):
    s, e = map(int,sys.stdin.readline().split())

    edge[s].append(e)
    edge[e].append(s)

# print(edge)
ans = bfs(1,0,computer)

print(ans-1)