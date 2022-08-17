import sys
sys.stdin = open('input.txt' , 'r')

# 절댓값 함수 구현
def abs_1(array):
    gap = array[0] - array[1]
    if gap >= 0:
        return gap
    else:
        return - gap

# len 함수 제작
def len_1(array):
    count = 0
    for a in array:
        count += 1
    return count

# 테스트 케이스 수 받아주기
T = int(input())

# 테스트 케이스 수만큼 반복
for t in range(T):
    N = int(input())
    applicants = [0] * N
    cnt = 0
    check = list()

    for n in range(N):
        applicants[n] = list(map(int, input().split()))
    
    applicants.sort(key=lambda x: (x[0], x[1]), reverse=True)

    for i in range(N):
        a, b = applicants[i][0], applicants[i][1]
        for j in range(i + 1, N):
            if applicants[j][0] > a and applicants[j][1] > b:
                check.append(applicants[j])
    
    print(len_1(check))


    '''
    score = applicants[-1]
    applicants.sort(key=lambda x: x[1])
    rank = applicants[-1]

    if abs_1(score) <= abs_1(rank):
        first = score
    else:
        first = rank

    check = list()
    print(first)
    for a in applicants:
        if a[0] < first[0] or a[1] < first[1]:
            cnt += 1
            check.append(a)
        else:
            pass
    '''