N, K = map(int, input().split())
arr = []
ranka = []
r = 0
m = 0
for i in range(K):
    arrv = list(map(int, input().split()))
    s = arrv.pop(0)
    arrv.sort()
    arr.append(arrv)

for j in range(K):

    rank_arr = []
    m = len(arr[j])-1
    r = arr[j][m]
    rank_arr.append(arr[j][m] + 1 + m)
    m -= 1
    while m != -1:
        if arr[j][m] == r:
            pass
        else:
            rank_arr.append(arr[j][m] + 1 + m)
            r = arr[j][m]
        m -= 1
    rank_arr.sort
    ranka.append(rank_arr)
    ranka[j].sort

for p in range(K):
    for q in range(len(ranka[p])):
        print(ranka[p][q], end=' ')
    print('')
