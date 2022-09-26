from collections import deque

# 먹을 수 있는 물고기인 걸 찾는 게 먼저가 아니라, 일단 갈 수 있는지 찾는 게 중요함
# 벽 구하는 코드는 그대로 사용해도 괜찮을 것 같음. 가장 중요한 건 bfs 만드는 것.
# 처음부터 bfs와 큐 적극적으로 사용할 것
# 이제 상위권 문제들은 대부분 큐랑 bfs 쓰는구나...

def find_shark(arr):
    global sea
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return [i, j]

def find_wall(arr):
    global walls
    for i in range(N):
        for j in range(N):
            if shark_size < arr[i][j]:
                walls.append([i, j])

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
second, shark_size, eat_count = 0, 2, 0
flag = False

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while True:
    ihere = find_shark(sea)
    fishes = list()
    walls = list()
    find_wall(sea)

    find_road = list()

    for i in range(N):
        for j in range(N):
            check = [[i, j]]
            if [i, j] not in walls:           
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if (0 <= ni < N) and (0 <= nj < N) and ([ni, nj] not in walls):
                            check.append([ni, nj])
            find_road.append(check)
    
    break
print(walls)
print(find_road)


'''

def find_shark(arr):
    global shark_is_here
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return [i, j]

def find_wall(arr):
    global fishes
    for i in range(N):
        for j in range(N):
            if shark_size < arr[i][j]:
                walls.append([i, j])

def go_to_eat(fish):
    global shark_is_here
    global sea
    global second
    global ihere
    global eat_count
    global flag

    present_position = ihere
    count = 0
    visited = list()
    while True:
        if flag:
            print(visited)
            break
        elif present_position == fish:
            sea[present_position[0]][present_position[1]] = 0
            second += count
            eat_count += 1
            print(visited)
            break
        else:
            can_go = list()
            i, j = present_position[0], present_position[1]

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < N) and (0 <= nj < N) and ([ni, nj] not in walls) and ([ni, nj] not in visited):
                    can_go.append([abs(fish[0] - ni) + abs(fish[1] - nj), [ni, nj]])
                    visited.append([ni, nj])
            
            if len(can_go) == 0:
                flag = True
                break
            else:
                can_go.sort()
                print(sea)
                print(can_go)
                shark_is_here[present_position[0]][present_position[1]] = 0
                present_position = can_go[0][1]
                shark_is_here[present_position[0]][present_position[1]] = 9
                count += 1
                print(shark_is_here)



N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
second, shark_size, eat_count = 0, 2, 0
flag = False

shark_is_here = [[0] * N for _ in range(N)]
ihere = find_shark(sea)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while True:
    ihere = find_shark(shark_is_here)
    fishes = list()
    walls = list()
    find_wall(sea)

    if len(fishes) == 0:
        break
    else:
        # 타켓 명확하게 지정
        for f in fishes:
            iwannaeat = fishes[0]
            if f[0] == iwannaeat[0]:
                if f[2][0] < iwannaeat[2][0]:
                    iwannaeat = f
                elif f[2][1] < iwannaeat[2][1]:
                    iwannaeat = f
        
        
        while ihere != iwannaeat[2]:
            cango = deque([(ihere[0], ihere[1])])
            moving = list()
            visited = [[0] * N for _ in range(N)]
            true = 0
            i, j = cango.popleft()
            visited[i][j] = 1

            while cango:
                findroad = list()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if (0 <= ni < N) and (0 <= nj < N) and ([ni, nj] not in walls) and (visited[ni][nj] == 0):
                        findroad.append((ni, nj))
                        visited[ni][nj] = 1
                

                
            if eat_count == shark_size:
                shark_size += 1
                eat_count = 0
    
print(walls)
print(shark_size)
print('sea')
print(sea)
print(second)

'''
