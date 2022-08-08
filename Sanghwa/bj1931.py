N = int(input())

schedule = []

# 입력된 회의의 시간대를 리스트로 만들어 저장
for i in range(N):
    tmp = list(map(int, input().split()))
    schedule.append(tmp)

# schedule리스트를 람다를 이용하여 정렬
# 해당 함수의 뜻으로는 schedule내부의 리스트의 두번째 값을 먼저 비교하여
# 오름차순으로 정렬 만약 두 값이 같으면 첫번째 값을 이용하여 오름차순 정렬
schedule.sort(key=lambda x:(x[1], x[0]))

cnt = 0
end = -1
# 정렬된 스케줄 리스트에서 만약 다음 회의의 시작 시간이 현재 진행중인
# 회의의 끝나는 시간보다 빠르다면 진행될 수 없다.
for i in schedule:
   if i[0] >= end:
    cnt += 1
    end = i[1] 

print(cnt)