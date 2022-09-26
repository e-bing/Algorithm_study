import sys
sys.stdin = open('sample_input.txt', 'r')

# 등산로 길이 확인할 f 함수 제작
def f(v, cnt):
    global can
    global answer

    # 만약 cnt + 1이 answer보다 크다면, answer에 cnt + 1한 값을 넣어줌
    if answer < cnt + 1:
        answer = cnt + 1

    # 현 좌표 i, j를 각각 설정해주고(v[0], v[1], v 자체가 좌표), visited에 방문 표시를 해줌
    i, j = v[0], v[1]
    visited[i][j] = 1
    
    # 델타 탐색 진행
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 만약 설정한 ni, nj 값이 범위 내에 있고, 아직 방문하지 않은 곳이라면, 이하 조건을 검증함
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            # 만약 해당 지형의 높이가 현재 지형 높이보다 높고, 아직 공사 가능성이 있으며, K 깊이만큼 공사가 가능하다면, 이하 절차를 거침
            # 이때 공사 깊이의 설정은 최대한 적은 값으로 설정(현재 지형 높이에서 -1한 값)
            if mapping[ni][nj] > mapping[i][j] and can == 1 and mapping[ni][nj] - (mapping[i][j] - 1) <= K:
                # 먼저 해당 지형의 높이 저장하고, can의 값을 0으로 설정
                # 나중에 다시 본래 값으로 초기화해주기 위해서임
                change = mapping[ni][nj]
                can = 0
                # 공사 가능한 깊이만큼 빼줌
                mapping[ni][nj] = mapping[i][j] - 1
                # 해당 지형 좌표 기준으로 재귀 진행함(cnt + 1해줌)
                f([ni, nj], cnt + 1)
                # 다시 본래 값으로 돌려놓은 후, can도 1로 초기화해줌
                mapping[ni][nj] = change
                can = 1
            # 만약 다음 지형 높이가 현재 지형 높이보다 낮다면, 그냥 아무 조건 설정하지 않고 진행해도 ㅇㅋ
            elif mapping[ni][nj] < mapping[i][j]:
                f([ni, nj], cnt + 1)
    # 모든 절차 끝낸 후 방문했던 기록 초기화해줌
    visited[i][j] = 0

# 테스트 케이스 수 받아줌
T = int(input())

# 테스트 케이스 수만큼 반복
for tc in range(1, T+1):

    # 지도의 가로 세로 길이 N, 최대 공사 가능 깊이 K를 받아줌
    N, K = map(int, input().split())
    # 현재 지도 상태를 N줄만큼 받아줌
    mapping = [list(map(int, input().split())) for _ in range(N)]
    # 정답이 될 아직 0인 변수 answer와 공사 가능 여부 can(딱 한 번)을 변수화
    answer = 0
    can = 1

    # 델타 탐색용 리스트 제작
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    # 최대값 구할 변수 maxv와 시작점이 될 리스트 start를 구해서 먼저 최대값부터 구한 후, 다시 2중 for문 돌려서 각 시작점을 start에 담아줌
    maxv = 0
    start = list()

    for i in range(N):
        for j in range(N):
            if mapping[i][j] > maxv:
                maxv = mapping[i][j]
    for i in range(N):
        for j in range(N):
            if mapping[i][j] == maxv:
                start.append([i, j])

    # 방문 여부 확인할 리스트 visited 생성
    visited = [[0] * N for _ in range(N)]

    # start에 들어있는 정점을 하나씩 꺼내서 미리 만들어둔 f함수에 넣고 출력
    for v in start:
        f(v, 0)

    # 모든 연산이 끝난 후, 정답을 출력함
    print('#{} {}'.format(tc, answer))