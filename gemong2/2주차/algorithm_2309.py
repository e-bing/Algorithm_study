nan_list = [int(input()) for _ in range(9)]
nan_sum = 0
not_nan1 = 0
not_nan2 = 0
for k in nan_list:
    nan_sum += k
nan_list.sort()

for i in range(9):
    for j in range(9):
        if nan_sum - nan_list[i] - nan_list[j] == 100 and i != j:
            not_nan1 = nan_list[i]
            not_nan2 = nan_list[j]
            break

for l in nan_list:
    if l != not_nan1 and l != not_nan2:
        print(l)




