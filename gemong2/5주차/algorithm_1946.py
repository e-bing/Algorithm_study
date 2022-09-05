import sys

T = int(sys.stdin.readline())


for _ in range(T):
    test_list = []
    interview_list = []
    cnt = 0
    N = int(sys.stdin.readline())
    for i in range(N):
        flag = 0
        test, interview = map(int, sys.stdin.readline().split())
        for j in range(len(test_list)):
            if test > test_list[j] and interview > interview_list[j]:
                flag = 1
                break

        test_list.append(test)
        interview_list.append(interview)
        if flag == 0:
            cnt += 1
    print(cnt)
