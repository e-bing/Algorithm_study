N, M = map(int, input().split())

arr = [0]*N


def check(arr):
    pass


for i in range(N):
    arr[i] = list(map(int, input().split()))

cnt = 1
zero = 0
while True:
    arr_c = arr.copy()
    for p in range(N):
        for q in range(N):
            if arr[p][q] != 0:
                if p-1 >= 0 and arr[p-1][q] == 0:
                    zero += 1
                if p+1 < N and arr[p+1][q] == 0:
                    zero += 1
                if q-1 >= 0 and arr[p][q-1] == 0:
                    zero += 1
                if q+1 < N and arr[p][q+1] == 0:
                    zero += 1
            arr_c[p][q] -= zero
            if arr_c[p][q] < 0:
                arr_c[p][q] = 0
            zero = 0

    check(arr)
    cnt += 1
