# BaekJoon 11729 하노이 탑 이동 순서
# 2022-08-07

def hanoi(start, dest, n):
    if n == 1: # 종료조건
        print(start, dest)
        return
    hanoi(start, 6-start-dest, n-1) # 다음 원반을 다른 기둥으로 이동
    print(start, dest) # 이번 원반의 이동을 표시
    hanoi(6-start-dest, dest, n-1) # 다 됐으면 다른 기둥에 있는 거 다시 옮겨오기

num = int(input()) # 원판의 개수 N
print(2 ** num - 1) # 최소 수행횟수
hanoi(1, 3, num) # 첫번째 기둥에서 세번째 기둥으로 이동


