# BaekJoon 2491 수열
# 2022-08-21

N = int(input())
data = list(map(int, input().split()))
up = 1
down = 1
max_value = 1
for i in range(N - 1):
    if data[i] < data[i + 1]:
        down += 1
        if up > max_value:
            max_value = up
        up = 1
    elif data[i] > data[i + 1]:
        up += 1
        if down > max_value:
            max_value = down
        down = 1
    elif data[i] == data[i + 1]:
        up += 1
        down += 1
if up > max_value:
    max_value = up
if down > max_value:
    max_value = down
print(max_value)