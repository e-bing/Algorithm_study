# BaekJoon 9205 맥주 마시면서 걸어가기
# 2022-09-05

T = int(input())
for tc in range(T):
    n = int(input())
    home = list(map(int, input().split()))
    conv_stores = [list(map(int, input().split())) for i in range(n)]
    festival = list(map(int, input().split()))
    queue = []
    visited = []
    result = 0
    queue.append(home)
    while queue:
        cur = queue.pop(-1)
        if abs(cur[0] - festival[0]) + abs(cur[1] - festival[1]) <= 1000:
            result = 1
            break
        for i in range(n):
            if i not in visited:
                new = conv_stores[i]
                if abs(cur[0] - new[0]) + abs(cur[1] - new[1]) <= 1000:
                    queue.append(new)
                    visited.append(i)

    if result:
        print('happy')
    else:
        print('sad')