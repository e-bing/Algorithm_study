a, b, price = map(int, input().split())

if b >= price:
    print(-1)
else:
    print(a // (price-b) + 1) # 손익분기점이므로 1 추가