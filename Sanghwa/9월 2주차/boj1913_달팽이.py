import math

N = int(input())
target = int(input())

board = [[0]*N for _ in range(N)]
si = N//2
sj = N//2

board[si][sj] = 1
ans_i, ans_j = 0 , 0

while si-1 >= 0 and sj-1 >= 0:
    si -= 1
    sj -= 1
    step = int(math.sqrt(board[si+1][sj+1])+2)
    board[si][sj] = step**2
    ni = si
    nj = sj
    for k in range(step-1):
        ni += 1
        board[ni][nj] = board[ni-1][nj]-1
    for k in range(step-1):
        nj += 1
        board[ni][nj] = board[ni][nj-1] -1
    for k in range(step-1):
        ni -= 1
        board[ni][nj] = board[ni+1][nj] -1
    for k in range(step-2):
        nj -= 1
        board[ni][nj] = board[ni][nj+1] -1


for i in range(N):
    for j in range(N):
        if board[i][j] == target:
            ans_i = i
            ans_j = j
        print(board[i][j], end=' ')
    print()

print(ans_i+1, end=' ')
print(ans_j+1)

