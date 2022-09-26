# def sum_i(arr):
#     total = 0
#     for a in arr:
#         total += arr[0]
#     return total

# def f(v):
#     if not visited[v] and stuff[v] not in stack:
#         visited[v] = 1
#         stack.append(stuff[v])
#         for j in range(v+1, N+1):
#             f(v)
#         visited[v] = 0
#         check.append(stack)

# 나눌 수 없는 knapsack(0-1) 알고리즘
# 이해 잘 못했음 ㅠ https://claude-u.tistory.com/208 설명 및 코드 참고
# DP 어렵다...
# 물품의 수 N와 버틸 수 있는 무게 K를 각각 입력받아줌
N, K = map(int, input().split())

# 초기값으로 [0, 0]가 든 stuff 리스트 설정해두고 N줄만큼 물건의 무게와 가치를 리스트 형태로 받아와 stuff에 추가해줌
stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

# DP용으로 사용할 0이 N + 1만큼 담긴 리스트를 K+1 줄 만큼 만들어줌
# 이렇게 하는 이유는 인덱스 에러 방지 및 계산 용이성을 위해 0번째 물건이 존재하며, 무게는 1부터 시작한다고 가정하는 것임
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 2중 for문 사용해 1부터 N+1만큼, 1부터 K+1만큼 반복함
# 현재 확인하고 있는 물건의 무게를 w, 가치를 v로 지정함
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = stuff[i][0], stuff[i][1]

        # 만약 현재 짊어지는 게 가능한 무게(j)가 w보다 작다면, 이전 인덱스에서 가능한 값을 들고 와서 넣어줌
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 만약 허용치가 w보다 크다면, 이 물건을 짊어져야 하는지 아닌지를 확인할 것임
        # i - 1(이전 물건), j에서 현재 무게를 뺀 값(그러니까 해당 무게를 짊어지고 있을 시점에서의 들 수 있는 최대치)에 현재 물건의 가치를 더한 값과 이전 이 무게였을 적의 최대치를 max로 비교함
        # 그러니까 이 물건을 들어야 하는가? 아닌가?의 검증이라고 보면 됨
        # 비교한 후 더 큰 값을 dp[i][j]에 넣어줌 
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

# 모든 연산이 끝난 후, 최대 값 출력
print(dp[N][K])