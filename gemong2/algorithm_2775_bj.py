# 1 4 10 20
# 1 3 6 10
# 1 2 3 4
#1시간 소요..

T = int(input())

i = 0
s = 0

while i < T:
    apart = list()
    k = int(input())
    n = int(input())
    for j in range(k+1):
        apart.append([])
        if j == 0:
            for u in range(n):
                apart[0].append(u+1)
#0층의 i호에는 i명이 산다고 해서 먼저 apart 리스트[0]에 주어진 n호 만큼 추가
        else:            
            for q in range(n):
                if q == 0:
                    s = 1
                    apart[j].append(1)
                else:
                    s += apart[j-1][q]
                    apart[j].append(s)
#0층이 아닌 층 중 1호라면 숫자 1을 집어넣고, 1호가 아니라면 아래 n호까지의 수를 더했다.
    i += 1
    print(apart[k][n-1])
    s = 0