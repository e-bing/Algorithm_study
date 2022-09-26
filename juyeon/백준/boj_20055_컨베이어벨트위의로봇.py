from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def belt_move():
    global conveyer
    cnt = 0
    for n in range(2 * N):
        if (check + n) > (2 * N - 1):
            conveyer[cnt] = [n + 1, arr[n]]
            cnt += 1
        else:
            conveyer[check + n] = [n + 1, arr[n]]

def robo_set():
    global robots
    global roborobo
    i = conveyer[0][0] - 1
    if arr[i] != 0 and i not in robots:
        arr[i] -= 1
        roborobo[i] = 1
        robots.append(i)

def robo_off():
    global robots
    global roborobo
    i = conveyer[N - 1][0] - 1
    if i in robots:
        roborobo[i] = 0
        robots.pop(robots.index(i))

def find_moving(arr):
    cnt = 0
    for a in arr:
        if a == 0:
            cnt += 1
    return cnt

def robot_move():
    global arr
    global robots
    global roborobo

    already_move = list()
    
    for i in robots:
        if i == N * 2 - 1:
            j = 0
        else:
            j = i + 1
        
        if arr[j] != 0 and (j not in robots) and (i not in already_move):
            print(i + 1, j + 1)
            arr[j] -= 1
            roborobo[i] = 0
            if j + 1 == conveyer[N - 1][0]:
                pass
            else:
                already_move.append(j)
                roborobo[j] = 1
            
    robots = already_move

T = int(input())

# 무조건 1번에서 올리고, N번에서 내린다
for tc in range(3):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # conveyer는 해당 번호 칸의 현재 위치를 나타내줌
    # robots는 로봇 배치 상황을 의미함
    conveyer = [0] * (2*N)
    robots = list()
    roborobo = [0] * (2*N)
    dont_move = 0
    stage = 0
    check = 0

    # while dont_move < K:

    while True:
        stage += 1
        if check == 2 * N - 1:
            check = 0
        else:
            check += 1
        belt_move()

        robo_off()
        robot_move()
        robo_set()


        print(stage)
        print(arr)
        print(conveyer)
        print(roborobo)
        print(robots)
        if find_moving(arr) >= K:
            break


    print('stage', stage)

