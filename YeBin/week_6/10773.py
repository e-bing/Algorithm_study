# BaekJoon 10773 제로
# 2022-09-13

import sys
sys.stdin = open('10773_input.txt', 'r')

K = int(input())
stack = []
for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop(-1)
    else:
        stack.append(num)
print(sum(stack))
