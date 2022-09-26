# 난 dfs와 bfs가 너무 싫다........
# dfs로는 해결되지 않음(백준에서 기본적으로 주어진 샘플 케이스에서 2번째 조건 충족 불가)
# bfs? but..........
# 백 트래킹 문제인 것 같은데 문제는 어떻게 구현하냐 이거지...............


# def f(v):
#     global cnt
#     global check

#     if len(stack) == 7:
#         if stack.count('S') >= 4:
#             print(stack)
#             check.append(stack)
#             check.append(think)
#             print(think)
#             cnt += 1
#         stack.pop()
#         think.pop()
#     else:
#         i, j = v[0], v[1]
#         if not visited[i*j-1]:
#             visited[i*j-1] = 1
#             stack.append(seat[i][j])
#             think.append(v)
#             for d in route[i][j]:
#                 f(d)
#             visited[i*j-1] = 0
#             if stack:
#                 stack.pop()
#                 think.pop()
#             else:
#                 return

# def dfs(v):
#     if len(stack) == 7:
#             print(stack)
#             check.append(stack)
#             check.append(think)
#             print(think)
#             cnt += 1
#             return
#     elif stack.count('Y') >= 4:
#         return
#     else:


# def nCr(n, r, s):
#     global think
#     if r == 0:
#         print(stack)
#     else:
#         for i in range(s, n-r+1):
#             stack[r-1] = road[i]
#             nCr(n, r-1, i+1)

def nCr(n, r, s):
    global check
    if r == 0 and stack not in think:
        think.append(stack)
        print(stack)
        print(*stack)
    else:
        for i in range(s, n-r+1):
            if r <= 0:
                break
            else:
                stack[r-1] = road[i]
                nCr(n, r-1, i+1)

seat = [[n for n in input()] for _ in range(5)]
cnt = 0
route = [[list() for _ in range(5)] for _ in range(5)]
road = list()

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
check = list()
cnt = 0
for i in range(5):
    for j in range(5):
        road.append(cnt)
        cnt += 1
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:
                route[i][j].append([ni, nj])

visited = [0] * 25
stack = [0] * 7
think = list()

# for i in range(5):
#     for j in range(5):
#         f([i, j])

print(road)
nCr(25, 7, 0)

print(len(road))
print(think)
