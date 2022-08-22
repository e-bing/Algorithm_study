# import sys
# sys.stdin = open('input.txt','r')

C, R = map(int, input().split())
K = int(input())
arr = [[0]* C  for _ in range(R)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ni = R-1 
nj = 0
turn = 3
correct = 0

for i in range(1, C * R + 1):
    arr[ni][nj] = str(i)
    if i == K:
        print(nj+1, abs(R-ni))
        correct = 1
        break
    ni += di[turn]
    nj += dj[turn]
    if 0 <= ni + di[turn] < R and 0 <= nj + dj[turn] < C and not arr[ni + di[turn]][nj + dj[turn]]:
        pass
    else:
        turn = (turn + 1) % 4

if correct == 0:
    print(0)
