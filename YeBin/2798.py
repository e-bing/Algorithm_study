num, goal = map(int, input().split()) # 숫자의 개수, 목표 수 설정
num_list = list(map(int, input().split())) # 입력된 수를 리스트로 만들어서 저장

max = 0 # 만들어진 수의 합을 담을 변수

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        for k in range(j + 1, len(num_list)):
            if max < num_list[i] + num_list[j] + num_list[k] <= goal: # max보다 크고 goal보다 작으면
                max = num_list[i] + num_list[j] + num_list[k] # max의 값을 업데이트

print(max)