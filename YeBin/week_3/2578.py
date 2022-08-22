# BaekJoon 2578 빙고
# 2022-08-22

def search_row(data):
    cnt = []
    for i in range(5):
        flag = 1
        for j in range(5):
            if data[i][j] != 0:
                flag = 0
                break
        if flag:
            cnt.append(i)
    return len(cnt)

def search_col(data):
    cnt = []
    for i in range(5):
        flag = 1
        for j in range(5):
            if data[j][i] != 0:
                flag = 0
                break
        if flag:
            cnt.append(i)
    return len(cnt)

def search_diag(data):
    flag_1 = 1
    flag_2 = 1
    for i in range(5):
        if data[i][i] != 0:
            flag_1 = 0
        if data[i][4 - i] != 0:
            flag_2 = 0
    return flag_1 + flag_2

data = [list(map(int, input().split())) for i in range(5)]
bingo = [list(map(int, input().split())) for i in range(5)]

for bingo_i in range(5):
    for bingo_j in range(5):
        find = 0
        for i in range(5):
            for j in range(5):
                if data[i][j] == bingo[bingo_i][bingo_j]:
                    data[i][j] = 0
                    find = 1
                    result = search_col(data) + search_row(data) + search_diag(data)
            if find:
                break
        if result >= 3:
            break
    if result >= 3:
        break
print((bingo_i) * 5 + bingo_j + 1)

