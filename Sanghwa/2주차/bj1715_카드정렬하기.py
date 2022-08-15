from queue import PriorityQueue

N = int(input())

cards = PriorityQueue()
total = 0

for i in range(N):
    cards.put(int(input()))

while cards.qsize() > 1:
    c1 = cards.get()
    c2 = cards.get()
    small = (c1 + c2)
    total += small
    cards.put(small)

print(total)

