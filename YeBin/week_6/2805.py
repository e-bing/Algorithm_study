# BaekJoon 2805 나무 자르기
# 2022-09-13

import sys
sys.stdin = open('2805_input.txt', 'r')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = sum(trees)

while start <= end:
    mid = (start + end) // 2
    length = 0
    for tree in trees:
        if tree > mid:
            length += tree - mid
    if length >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
