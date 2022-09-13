N = int(input())
M = int(input())
di = [-1, 0, 1, 0]  # 상 우 하 좌
dj = [0, 1, 0, -1]

arr = [[0] * N for _ in range(N)]

ai = N//2
aj = N//2
arr[ai][aj] = 1

k = 2
row = 1
turn = 0
answer = []
if M == 1:
    answer = [N//2, N//2]
while k <= N*N:

    if ai+di[turn] < N//2 - row or ai+di[turn] > N//2 + row or aj+dj[turn] < N//2 - row or aj+dj[turn] > N//2 + row:
        turn += 1
        if turn == 4:
            turn = 0

    if arr[ai+di[turn]][aj+dj[turn]] != 0:
        turn += 1
        if turn == 4:
            turn = 0

        if k == M:
            answer.append(ai+di[turn] + 1)
            answer.append(aj+dj[turn] + 1)

        arr[ai+di[turn]][aj+dj[turn]] = k
        ai = ai+di[turn]
        aj = aj+dj[turn]
    else:
        if k == M:
            answer.append(ai+di[turn] + 1)
            answer.append(aj+dj[turn] + 1)

        arr[ai+di[turn]][aj+dj[turn]] = k
        ai = ai+di[turn]
        aj = aj+dj[turn]

    k += 1

    if (k**(1/2)) % 2 == 1:
        row += 1

for p in range(N):
    for q in range(N):
        print(arr[p][q], end=' ')
    print('')
print(*answer)


# if arr[ai][aj] == 0:
#     arr[ai][aj] = k
#     if k == M:
#         answer[0] =
#     k += 1
# if abs(ai + di[num] - N//2) != row or abs(aj + dj[num] - N//2) != row:
#     num += 1
# if num == 4:
#     num = 0
# ai += di[num]
# aj += dj[num]

# if (k**(1/2)) % 2 == 1:
#     row += 1
# for i in range(N):
#     for j in range(N):
#         if num < k:
#             ni = i + di[3]
#             nj = j + dj[3]
#         else:
#             num = 0

#         arr[ni][nj] = k
#         num += 1
#         k += 1
