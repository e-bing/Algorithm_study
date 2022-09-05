# BaekJoon 2606 바이러스
# 2022-09-04

N = int(input())
pairs = int(input())
computers = [[] for i in range(N)]
visited = []
stack = []
for i in range(pairs):
    n, m = map(int, input().split())
    computers[n - 1].append(m-1)
    computers[m - 1].append(n-1)
if computers[0]:
    stack.append(0)
    i = 0
    while len(stack) > 0:
        flag = 1
        if i not in visited:
            visited.append(i)
        for cur in computers[i]:
            if cur not in visited:
                if cur != computers[i][-1]:
                    stack.append(i)
                i = cur
                flag = 0
                break
        if flag:
            i = stack.pop(-1)
    print(len(visited) - 1)

else:
    print(0)
