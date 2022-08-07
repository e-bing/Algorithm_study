
"""
너무 복잡하게 생각해서 결국 못풀음 규칙을 하나하나 다 정리해서 for문과 if문을 활용하려함
재귀함수의 개념이 아직 부족하다 ㅜ


내가 찾은 규칙

1. 빈 리스트가 두개 일 때, 짝수면 처음 빈칸에, 홀수면 두번재 빈칸에 원판을 둔다.(맨처음만 해당)
2. 바로 전 이동한 원판은 이동 금지
3. 옮길 수 있는 곳이 한 곳이라면 거기에 원판 두기
4. 두 곳에 옮길 수 있다면 (숫자, 숫자) 
(1) 옮기려는 숫자와 1차이 나는 숫자가 있다면 그 곳에 원판두기
(2) 둘다 2 이상 차이 난다면 
<1> 내 밑숫자, 밑밑밑 숫자 등 홀수번째 숫자와 1차이 난다면 1차이가 아닌 곳에 원판두기
<2> 내 밑밑숫자, 밑밑밑밑 숫자 등 짝수번째 숫자와 1차이 난다면 1차이나는 곳에 원판두기
4-1. 두 곳에 옮길 수 있다면 (숫자, 공백)
(1) 옮기려는 숫자와 1차이 나는 숫자가 있다면 그 곳에 원판두기
(2) 둘다 아니라면 (공백이거나 2이상차이)
<1> 내 밑숫자, 밑밑밑 숫자 등 홀수번째 숫자와 1차이 난다면 공백에 원판두기
<2> 내 밑밑숫자, 밑밑밑밑 숫자 등 짝수번째 숫자와 1차이 난다면 숫자에 원판두기

"""


k = int(input())
board = [[*range(1,k+1)],[],[]]
s = board[0][0]
if k % 2 == 0:
    board[1].append(s)
    board[0].pop(0)
    count = 1
else:
    board[2].append(s)
    board[0].pop(0)
    count = 1
num = 0
bnk = 0
another = 0
cnt = 0
while True:
    for i in board:
        i.sort()
    for j in board:
        if i[0] != s:
            for l in board:
                if l != 0:
                    if i[0] < l[0]:
                        num += 1
                    else:
                        pass
                else:
                    pass

            if num == 1:
                s = i[0]
                for l in board:
                    if l != 0:
                        if i[0] < l[0]:
                            l[0].append(s)
                            i[0].pop
                            num = 0
                            count += 1
                        else:
                            pass
                    else:
                        pass
                
            if num == 2:
                s = i[0]
                for n in board:
                    if n == 0:
                        bnk +=1
                    else:
                        pass
                if bnk == 0:
                    for l in board:
                        if i[0] < l[0]:
                            if i[0] - l[0] == 1:   
                                l[0].append(s)
                                i[0].pop
                                num = 0
                                count += 1
                            else:
                                for q in board:
                                    for w in i:
                                        if w - q[0] == 1:
                                            another = q[0]
                                            cnt = board.index(w)
                                            if cnt % 2 == 0:
                                                q[0].append(s)
                                                i[0].pop
                                                num = 0
                                                count += 1
                                            else:
                                                for u in board:
                                                    if q[0] != u[0] and i[0] != u[0]:
                                                        u[0].append(s)
                                                        i[0].pop
                                                        num = 0
                                                        count += 1
                else:
                    for l in board:
                        if l != []:
                            if i[0] < l[0]:
                                if i[0] - l[0] == 1:   
                                    l[0].append(s)
                                    i[0].pop
                                    num = 0
                                    bnk = 0
                                    count += 1
                                else:
                                    for q in board:
                                        for w in i:
                                            if q != []:
                                                if w - q[0] == 1:
                                                    cnt = board.index(w)
                                                    if cnt % 2 == 0:
                                                        for y in board:
                                                            if y != [] and i[0] != y[0]:
                                                                y[0].append(s)
                                                                i[0].pop
                                                                num = 0
                                                                bnk = 0
                                                                count += 1
                                                    else:
                                                        for u in board:
                                                            if u == []:
                                                                u[0].append(s)
                                                                i[0].pop
                                                                num = 0
                                                                bnk = 0
                                                                count += 1
                            else:
                                pass
                        else:
                            pass
            else:
                pass
        else:
            pass
    if board[2] == list(range(1,k+1)):
        print(count)
        break

