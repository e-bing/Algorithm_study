# 5658_보물상자 비밀번호 풀이
# # 2022-08-19

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(input())
    key_arr = []
    num_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    hex_arr = ['A', 'B','C', 'D', 'E', 'F']
    rotate = 0
    result = 0
    while rotate < N // 4:
        for i in range(4):
            tmp = ''
            for j in range(i * (N // 4), (i + 1) * (N // 4)):
                tmp += arr[j]
            key_arr.append(tmp)
        arr.insert(0, arr.pop(-1))
        rotate += 1
    key_arr = list(set(key_arr))
    key_arr.sort(reverse=True)
    for i in range(len(key_arr[K - 1])):
        if key_arr[K - 1][i] in num_arr:
            result += int(key_arr[K - 1][i]) * 16**(len(key_arr[K - 1]) - 1 - i)
        else:
            result += (hex_arr.index(key_arr[K - 1][i]) + 10) * 16 ** (len(key_arr[K - 1]) - 1 - i)
    print('#{} {}' .format(tc, result))