# BaekJoon 2606 바이러스
# 2022-08-22

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self, item):
        self.stack.append(item)
        self.top += 1
    
    def pop(self):
        if self.top < 0:
            return None
        else:
            self.top -= 1
            return self.stack.pop(-1)

num = int(input())
pairs = int(input())
my_stack = Stack()
visited = [False] * num
next = [[]] * num
for i in range(num):
    my_stack.push(i)
for i in range(pairs):
    start, dest = map(int, input().split())
    next[start - 1].append(dest)
    next[dest - 1].append(start)
print(next)

