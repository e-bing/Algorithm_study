N = int(input())

arr = list(map(int, input().split()))

arr.sort()
print(arr[(N - 1)//2])
# cnt_a = 0
# cnt_b = 0
# dup = 0
# if N % 2 == 0:
#     a = arr[N//2-1]
#     for i in arr:
#         cnt_a += abs(i-a)
#     a = arr[N//2]
#     for j in arr:
#         cnt_b += abs(j-a)

#     if cnt_a <= cnt_b:
#         print(arr[N//2 - 1])
#     else:
#         print(arr[N//2])
# else:
#     print(arr[N//2 - 1])
