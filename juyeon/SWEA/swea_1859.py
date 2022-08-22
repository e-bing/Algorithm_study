import sys
sys.stdin = open('input.txt', 'r')

# 총 테스트 케이스 번호 입력받아 T에 저장
T = int(input())

# T만큼 테스트 케이스 반복
for t in range(T):
    
    # 총 날짜 N 받아주기 
    N = int(input())

    # 날짜별 매매 상황 arr에 담아주기
    arr = list(map(int, input().split()))
    # 효율적으로 매매할 시 최대값을 담아줄 total 변수 생성해주기
    total = 0

    # 뒤에서부터 보는 것이 연산이 더 간단해지므로 arr의 앞뒤를 반전해줌
    arr = arr[::-1]

    # maxv 변수에 arr의 첫 값(그러니까 맨 마지막 날 매매가)을 넣어줌
    maxv = arr[0]

    # 가장 마지막 날은 사실상 매매의 의미가 없으므로 1부터 N 사이로 범위지정한 후 for문을 돌림
    # 만약 해당 인덱스의 값이 maxv보다 작거나 같다면 매매를 해도 괜찮거나 사고 파는 거 자체가 의미가 없다는 뜻임(같으면 팔아도 0)
    # 따라서 더 큰 값이 나올 때까지 maxv값에 당일 매매값을 빼준 값을 total에 더해줌
    # 만약 더 큰 값이 나왔다면, maxv 변수를 arr[a]로 갱신함
    for a in range(1, N):
        if maxv < arr[a]:
            maxv = arr[a]
        else:
            total += maxv - arr[a]

    # 모든 연산이 끝난 후, 지정된 형식에 따라 값 출력
    print('#{} {}'.format(t+1, total))
