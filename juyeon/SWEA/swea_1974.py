T = int(input())

for t in range(T):
    number_list = list()
    true_false = 0
    
    for n in range(9):
        a = input().split()
        number_list.append(a)

# 가로 합계 구한 후, 45(1~9까지의 총합계)가 아니면 true_false에 1씩 더해줌
    for n in a:
        if sum(a) == 45:
            pass
        else:
            true_false += 1

# 세로 합계 구한 후, 45(1~9까지의 총합계)가 아니면 true_false에 1씩 더해줌
    for n in range(9):
        check = list()
        for i in range(9):
            check.append(number_list[i][n])
        if sum(check) == 45:
            pass
        else:
            true_false += 1

# 여기까지는 괜찮은데 이제 스토쿠 3x3 정사각형 로직을 어떻게 짜야 할지 잘 모르겠습니다...
# 슬라이싱 해서 각 부분만 합계 구하면 될 것 같긴 한데 for문이 너무 많이 들어가서 난잡하고, print로 확인해봐도 어디서부터 잘못된건지 모르는 난감한 상태...
    numbers = [0, 3, 6]
    
    for x in range(3):
        for n in range(numbers[x], numbers[x] + 3):
            check = list()
            for y in range(3):
                for i in range(numbers[y], numbers[y] + 3):
                    check.append(number_list[n][i])
            if sum(check) == 45:
                pass
            else:
                true_false += 1


    if true_false > 0:
        print(f'#{t + 1} 0')
    else:
        print(f'#{t + 1} 1')
