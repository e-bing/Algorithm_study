# BaekJoon 2757 엑셀
# 2022-08-14

def convert(num):
    result = ''
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num >= 27:
        result = convert((num - 1) // 26)
    result += base[num % 26 - 1]
    return result

data = []
while True:
    data.append(list(map(int, input()[1:].split('C'))))
    if (data[-1][0] == 0) and (data[-1][1] == 0):
        break

data.pop()
for i in data:
    i[1] = convert(i[1])
    print(i[1] + str(i[0]))