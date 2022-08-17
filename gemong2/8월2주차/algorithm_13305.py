import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
sum_road = 0
gas_price = 0
j = 0

while j < len(road):

    if j + 1 < len(road) and price[j] > price[j+1]:
        gas_price += price[j] * road[j]
        j = j+1
    elif j == len(road) - 1:
        gas_price += price[j] * road[j]
        j = j+1

    elif j + 1 < len(road) and price[j] < price[j+1]:
        gas_price += price[j] * (road[j] + road[j + 1])
        cnt = 0
        for l in range(j+2, len(road)):
            if price[j] >= price[l]:
                j = j + 2 + cnt
                break
            else:
                gas_price += price[j] * road[l]
                cnt += 1

print(gas_price)

# def min_price(start, price):
#     min_gas = price[0]
#
#     for i in range(start,len(price)):
#         if min_gas > i:
#             min_gas = i
#     return min_gas

# if price[j] == min_price(j,price):
#     for k in range(j, len(road)):
#         sum_road += k
#     gas_price += price[j] * sum_road
#     break

