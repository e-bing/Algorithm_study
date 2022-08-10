# 손익분기점을 구하는 문제임.
# 고로 총 수입 - 총 비용이 0 이상이 되는 시점의 판매량을 구할 필요가 있음.

# 먼저 A(고정 비용), B(가변 비용), C(제품 가격)을 리스트 형태로 입력 받아줌.
# 동시에 map을 이용해 리스트 내용물을 int(정수)화 해줌
numbers = list(map(int,input().split()))

# 입력 받은 값이 담긴 리스트 내의 요소들을 각각 역할에 맞게 A, B, C 변수 안에 집어 넣어 줌.
A, B, C = numbers[0], numbers[1], numbers[2]

# 여기서 먼저 따져봐야 할 것이 있는데, 가변 비용 B와 제품 가격 C는 고정 비용 A와 달리 제품 하나를 판매할 때마다 동시에 변동이 생기는 값이기도 함.
# 따라서 제품 가격이 가변 비용보다 낮다면, 이익이 지출을 따라잡는 것이 사실상 불가능하기에 손익 분기점 자체가 생성되지 않음.
# 지시사항에 따르면 손익 분기점이 주어지지 않을 경우에는 -1을 출력해야 함
# if문을 사용해, 제품 가격이 가변 가격보다 클 가능성(손익 분기점 존재)과 작을 가능성(존재 x)를 나눠서 작성해줌.
if C > B:
    # 만약 손익 분기점이 존재할 시, C - B하여 순수한 이익만 담은 변수 profit을 만들어줌.
    profit = C - B
    # 고정 비용을 순이익 profit으로 나눠주고, 여기에 +1하여 조건에 맞는 총 판매량 값을 출력함
    # 최초로 총 수익이 총 지출을 넘어서는 지점을 구하라고 하였으므로, 0 이하 값은 제외되어야 함을 알 수 있음.
    print((A // profit) + 1)

else:
    # 만약 제품 가격이 가변 비용보다 낮다면, 손익 분기점이 존재하지 않는다는 뜻이므로 -1을 출력함.
    print(-1)


