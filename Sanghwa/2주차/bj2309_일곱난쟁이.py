shorts = []
fake = []
for i in range(9):
    shorts.append(int(input()))
total = sum(shorts)

for i in range(len(shorts)-1):
    if len(fake) == 2:
        break
    for j in range(i+1, len(shorts)):
        if total - (shorts[i] + shorts[j]) == 100:
            fake.append(shorts[i])
            fake.append(shorts[j])
            break

shorts.remove(fake[0])
shorts.remove(fake[1])
shorts.sort()

for i in shorts:
    print(i)