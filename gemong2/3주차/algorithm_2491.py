T = int(input())


arr = list(map(int, input().split()))
cnt_p = 1
cnt_m = 1
max_cnt_p = 1
max_cnt_m = 1

for i in range(T-1):
    if arr[i] >= arr[i+1]:
        cnt_m += 1
    else:
        if cnt_m > max_cnt_m:
            max_cnt_m = cnt_m
        cnt_m = 1

for j in range(T-1):
    if arr[j] <= arr[j+1]:
        cnt_p += 1
    else:
        if cnt_p > max_cnt_p:
            max_cnt_p = cnt_p
        cnt_p = 1
if cnt_m > max_cnt_m:
    max_cnt_m = cnt_m
if cnt_p > max_cnt_p:
    max_cnt_p = cnt_p
if max_cnt_m >= max_cnt_p:
    print(max_cnt_m)
else:
    print(max_cnt_p)