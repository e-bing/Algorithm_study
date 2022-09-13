def make_code(depth, result, idx):
    if depth == L:
        odd_cnt = 0                              # 모음의 개수
        even_cnt = 0                             # 자음의 개수
        for lt in result:
            if lt in odd:
                odd_cnt += 1
            else:
                even_cnt += 1
        if odd_cnt >=1 and even_cnt >= 2:       # 최종 모음의 개수와 자음의 개수가 조건을 충족하면 출력
            print(''.join(result))
            return

    for i in range(idx, C):
        result.append(letters[i])              # 글자 하나를 넣어 다음 단계로 전달하기 위한 것
        make_code(depth+1, result, i+1)        # 다음 번째 글자를 정하기 위한 재귀
        result.pop()                           # 같은 위치에 다른 글자를 넣기 위해 글자를 리스트에서 제거


L, C = map(int, input().split())

letters = list(input().split())
odd = ['a','e','i','o','u']
letters.sort()

make_code(0,[],0)



