import sys
sys.stdin = open('input.txt','r', encoding= 'UTF-8')

bingo = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5):
    mc += list(map(int, input().split())) 

def bingocheck(bingo):
    lines = 0
    cross_cnt, line_cnt = 0, 0
    for p in range(5):
        if bingo[p][p] == 0:
            cross_cnt += 1
        if bingo[4-p][p] == 0:
            line_cnt += 1
        row_cnt, col_cnt = 0 ,0
        for q in range(5):
            if bingo[p][q] == 0:
                row_cnt += 1
            if bingo[q][p] == 0:
                col_cnt += 1
        if row_cnt == 5:
            lines += 1
        if col_cnt == 5:
            lines += 1
    if cross_cnt == 5:
        lines += 1
    if line_cnt == 5:
        lines += 1
    if lines >= 3:
        return True
    else:
        return False

for u in range(25):
    for i in range(5):
        for j in range(5):
            if mc[u] == bingo[i][j]:
                bingo[i][j] = 0

    if u >= 11:
        if bingocheck(bingo):
            print(u+1)
            break

