import copy

def dfs(board):
    global answer
    if depth == len(cctv_dir):
        cnt = 0
        for i in range(N):
            cnt += board[i].count(0)
        answer = min(answer, cnt)
        return

    tmp = copy.deepcopy(board)


N, M = map(int, input().split())

board = list(list(map(int,input().split())) for _ in range(N))

dir_list = [(-1,0), (1,0), (0,-1), (0,1)]

cctv_dir = [
    [],
    [[0],[1],[2],[3]], # 1번 cctv
    [[0,1],[2,3]], # 2번 cctv
    [[0,1,2],[0,2,3],[0,1,3],[1,2,3]], # 3번 cctv
    [[0,1,2,3]], # 4번 cctv
]