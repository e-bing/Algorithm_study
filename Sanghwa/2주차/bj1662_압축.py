zipped = input()
stack = []
total = 0

for i in range(len(zipped)):
    if i != len(zipped)-1 and zipped[i+1] == '(':
        stack.append(int(zipped[i]))
    elif zipped[i] == '(':
        stack.append('(')
    elif zipped[i] == ')':
        now = 0
        while stack[len(stack)-1] != '(':
            if stack[len(stack)-1] == '+':
                now += 1
                stack.pop()
            else:
                now += stack.pop()
        stack.pop()
        tmp = stack.pop()*now
        if tmp != 0:
            stack.append(tmp)

    else:
        stack.append('+')

while len(stack) != 0:
    if stack[len(stack)-1] == '+':
        total += 1
        stack.pop()
    else:
        total += stack.pop()

print(total)