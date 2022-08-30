T = int(input())

for tc in range(1,T+1):
    N = int(input())
    K = int(input())
    
    arr = list(input())
    check = []
    top = 0
    rear = N-1
    i = 0
    while i <= N:
        for j in range(N//4):
            check[i].append(arr[top])
    
    #4로 나눈 값만큼 리스트를 만들어서 묶음을 모두 리스트에 넣어주고
    #값을 오름차순으로 정리해서 순위비교