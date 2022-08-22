# BaekJoon 9663 N-Queen
# 2022-08-22

def check(N, data, cur, num):
    for i in range(cur):
        diff = cur - i
        if data[i] == num:
            return False
        elif (data[i] + diff < N) and (data[i] + diff == num):
            return False
        elif (data[i] - diff >= 0) and (data[i] - diff == num):
            return False
    return True

def set_location(board, idx, N):
    result = 0
    if idx == N:
        return 1
    else:
        for num in range(N):
            if check(N, board, idx, num):
                board[idx] = num
                result += set_location(board, idx + 1, N)
    return result

N = int(input())
board = [0] * N
rst = set_location(board, 0, N)
print(rst)

