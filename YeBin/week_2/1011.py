# BaekJoon 1011 Fly me to the Alpha Centauri
# 2022-08-16

T = int(input())
data = []
for tc in range(T):
    data.append(list(map(int, input().split())))

for tc in range(T):
    dist = data[tc][1] - data[tc][0]
    sum = 0
    for i in range(1, dist + 1):
        sum += i
        if dist <= sum:
            result = i * 2 - 1
            break
        sum += i
        if dist <= sum:
            result = i * 2
            break
    print(result)