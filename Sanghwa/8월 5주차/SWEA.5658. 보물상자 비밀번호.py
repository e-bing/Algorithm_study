for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    numbers = list(input())

    pws = set()

    before = len(pws)

    while True:
        tmp = numbers[N - 1:]
        tmp2 = numbers[:N - 1]
        numbers = tmp + tmp2
        for i in range(0, N, N // 4):
            num = ''
            for j in range(N // 4):
                num += numbers[i + j]
            pws.add(num)

        if before == len(pws):
            break
        else:
            before = len(pws)

    maxV = 0
    ans = []
    for i in list(pws):
        ans.append(int(i, 16))

    ans.sort(reverse=True)

    print("#{} {}".format(tc, ans[K-1]))