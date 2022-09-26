# 2차원 배열의 총합을 구하는 함수 sum_i 임의 제작
def sum_i(room):
    total = 0
    for i in range(R):
        for j in range(C):
    # 만약 해당 좌표의 값이 -1(공기청정기 위치)나 0이 아니라면 total에 해당 값을 더해줌
            if room[i][j] != -1 and room[i][j] != 0:
                total += room[i][j]
    return total

# 미세먼지의 확산을 함수화
# 먼저 room(현재 집의 상황 입력을 받아온 2차원 배열)과 크기가 같은 2차원 배열 change를 임의 제작함
# 2중 for문 사용하여 room 모두 순회함
def fine(room):
    change = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 만약 현재 좌표가 공기청정기의 위치가 아니고, 미세먼지가 존재한다면, 확산할 필요가 있음
            # 주변에 주어야 하는 값(해당 좌표의 값을 5로 나눈 것(나머지 존재 x))을 give 함수에 담아줌
            # 이번 문제에서는 조건에 따라 미세먼지가 퍼지지 않아야 하는 곳도 있으므로, 몇 칸에 퍼지는지 확인해줄 변수 cnt를 제작
            if room[i][j] != -1 and room[i][j] != 0:
                give = room[i][j] // 5
                cnt = 0
                # 미세먼지는 상하좌우 한 칸씩 퍼짐. 델타 탐색 진행함.
                # for문 이용해 4방향의 좌표 변화값을 미리 지정해둔 리스트 di, dj의 값을 불러와 각각 i와 j에 더해줌
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 만약 ni, nj의 값이 집의 범위를 벗어나거나, 공기청정기의 위치가 아니라면 확산!
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                    # 해당하는 경우 cnt에 1씩 더해준 후, change의 해당 좌표 값에 give를 더해줌
                        cnt += 1
                        change[ni][nj] += give
                # 모든 탐색이 끝나면, 현재 좌표 값에 분배해준 미세먼지만큼의 값을 빼줌
                change[i][j] += room[i][j] - (give * cnt)
            # 만약 해당 위치에 공기 청정기가 위치해있다면, change에도 반영해줌
            # room를 change로 대체할 생각이기 때문임
            elif room[i][j] == -1:
                change[i][j] = -1
    # 모든 변화가 끝난 change를 return해줌
    return change

# 공기청정기의 작동을 함수화
# 함수를 불러오는 쪽이 시간이 더 걸리는데다 room를 직접 건드는 것도 괜찮기 때문에(미세먼지 확산의 경우 동시 발생이라 불가) 함수화 굳이 안해도 될지도?
# 먼저 room를 글로벌 선언해주고, 미리 구해뒀던 공기청정기의 위아래 좌표를 각각 변수 air_top, air_bottom에 할당해줌
def air_push():
    global room
    air_top = air_con[0]
    air_bottom = air_con[1]

    # 2만큼 반복
    # 만약 a가 0이라면, 공기는 반시계방향으로 순환함
    for a in range(2):
        if a == 0:
    # i, j를 현재 공기청정기의 바로 오른쪽 칸의 좌표로 지정해둠
    # 굳이 공기청정기 좌표가 아니라 오른쪽으로 지정한 것은 탈출 조건과 관련이 있기 때문임!
    # 방향 바꿀 때마다 델타탐색 때처럼 간섭해줄 변수 x, y를 지정함
    # 이동해야 하는 미세먼지의 값을 dust 변수에 담아준 후, room[i][j] 값을 0으로 초기화해줌(공기청정기 바로 다음 칸이므로 이동할 미세먼지 x)
            i, j = air_top[0], air_top[1] + 1
            x, y = 0, 1
            dust = room[i][j]
            room[i][j] = 0
    # while문 사용해서 조건 만족시때까지 계속 반복함
    # for문 써도 괜찮을 것 같긴 한데 추가로 (인간뇌로) 계산 필요해서 번거로울 듯?
            while True:
    # i와 j에 각각 x와 y값을 더해줌(공기 순환 방향대로 미세먼지 이동)
    # 만약 현 좌표값이 공기청정기 상부가 위치한 좌표와 일치하다면, 해당 좌표의 값을 -1로 변화시킨 후, break함
    # -1로 바꿔주지 않는다면, 이후에 진행되는 계산식 영향으로 0이 되는 바람에 2회차 이상일 시 여기에도 미세먼지 할당될 수 있으니 주의
                i += x
                j += y
                if [i, j] == air_top:
                    room[i][j] = -1
                    break
    # 만약 공기청정기가 위치하지 않았다면, 미세먼지 이동을 진행함
    # 현재 미세먼지 값과 room[i][j]의 값을 파이써닉한 방법을 이용해 서로 교체해줌
                else:
                    room[i][j], dust = dust, room[i][j]

    # 만약 해당 좌표 값이 순환방향을 변경해야 하는 좌표 값이라면, if문을 통해 바꿀 방향을 결정함
    # 바람이 오른쪽으로 이동(시작값)하다 위로 방향을 변경해야 할 때는, x와 y의 값을 각각 -1, 0으로 변경
                    if [i, j] == [air_top[0], C - 1]:
                        x, y = -1, 0
    # 바람이 위에서 왼쪽으로 꺾어야 한다면, x와 y값을 각각 0과 -1로 변경
                    elif [i, j] == [0, C - 1]:
                        x, y = 0, -1
    # 마지막으로 바람이 왼쪽에서 아래로 향한다면, x와 y 값을 각각 1과 0로 변경
                    elif [i, j] == [0, 0]:
                        x, y = 1, 0
    
    # 이하 if문은 공기청정기 하부의 조건식으로, 바람의 방향이 시계방향으로 변경된다는 점만 제외하고는 동일함
        if a == 1:
            i, j = air_bottom[0], air_bottom[1] + 1
            x, y = 0, 1
            dust = room[i][j]
            room[i][j] = 0
            while True:
                i += x
                j += y
                if [i, j] == air_bottom:
                    room[i][j] = -1
                    break
                else:                
                    room[i][j], dust = dust, room[i][j]
                    if [i, j] == [air_bottom[0], C - 1]:
                        x, y = 1, 0
                    elif [i, j] == [R - 1, C - 1]:
                        x, y = 0, -1
                    elif [i, j] == [R - 1, 0]:
                        x, y = -1, 0


# 방의 세로 길이(R), 방의 가로 길이(C), 순환하는 초(T)를 입력받아 각각 해당하는 변수에 담아줌
R, C, T = map(int, input().split())
# 방의 상황을 2차원 배열 room에 담아줌
room = [list(map(int, input().split())) for _ in range(R)]

# 델타탐색용 리스트 di, dj 제작
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 공기청정기의 좌표를 담아줄 air_con 리스트 생성한 후, 만약 상부 공기청정기를 찾았다면, 하부 공기청정기도 바로 아래에 붙어 있기에 그 즉시 둘 모두 추가해준 후 break로 빠져나와줌
# 문제에 공기 청정기는 항상 1번 열에 설치되어 있다고 했으므로, for 반복문은 한번만 사용해도 괜찮음
air_con = []
for i in range(R):
    if room[i][0] == -1:
        air_con.append([i, 0])
        air_con.append([i+1, 0])
        break

# for문을 이용해 T초만큼 미세먼지 확산과 공기청정기 작동을 차례대로 진행함
for t in range(T):
    room = fine(room)
    air_push()
    
# 모든 활동이 끝난 후, room에 남은 미세먼지의 양을 미리 만들어둔 sum_i 함수를 이용해 구한 후 출력함
print(sum_i(room))