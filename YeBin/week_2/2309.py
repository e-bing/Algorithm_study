# BaekJoon 2309 일곱 난쟁이
# 2022-08-14

heights = []
for i in range(9):
    heights.append(int(input()))

diff = sum(heights) - 100

flag = 1
for first in range(9):
    for second in range(first + 1, 9):
        if heights[first] + heights[second] == diff:
            flag = 0
            heights.remove(heights[second])
            heights.remove(heights[first])
            break
    if flag == 0:
        break

heights.sort()

for i in heights:
    print(i)