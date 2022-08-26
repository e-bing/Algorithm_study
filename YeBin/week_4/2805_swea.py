# SWEA 2805 농작물 수확하기
# 2022-08-26

import sys
sys.stdin = open('2805_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    money = [list(map(int, input())) for i in range(N)]
    sum_value = 0
    for i in range(N // 2):
        for j in money[i][N//2 - i:(N + 1)//2 + i]:
            sum_value += j
    for j in money[N // 2][0:N]:
        sum_value += j
    for i in range(1, N // 2 + 1):
        for j in money[N // 2 + i][i:N-i]:
            sum_value += j
    print('#{} {}'.format(tc + 1, sum_value))
