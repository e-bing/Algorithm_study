N, K = map(int, input().split())
arr = []
rank = []
for i in range(K):
    arr[i] = map(int, input().split())
    arr[i].sort

for j in range(K):
    for l in range(len(arr[j])):
        if arr[j][l] == 4:
            pass
