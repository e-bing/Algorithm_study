# BaekJoon 2757 엑셀
# 2022-08-14

data = []
while True:
    data.append(list(map(int, input()[1:].split('C'))))
    if (data[-1][0] == 0) and (data[-1][1] == 0):
        break

data.pop()
print(data)
for i in data:
    for j in range(i[1] // 27 + 1):
        print(i[1] % 27 + 64, chr(i[1] % 27 + 64), end='')
        i[1] -= 26
    print()
