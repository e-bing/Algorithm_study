S = input()
q = int(input())
arr = [list(input().split()) for _ in range(q)]

for i in range(q):
    j = int(arr[i][1])
    k = int(arr[i][2])
    cnt = 0
    for a in range(j,k+1):
        if arr[i][0] == S[a]:
            cnt += 1
    print(cnt)
