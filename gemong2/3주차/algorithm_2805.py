N, M = map(int,input().split())

tree = list(map(int, input().split()))
'''

high_tree = tree[0]
 
for i in range(N):
    if tree[i] > high_tree:
        high_tree = tree[i]
start = 0
end = high_tree
'''
start = 0
end = max(tree)
answer = 0
while start <= end:
    cnt = 0
    mid = (start+end) // 2

    for j in tree:
        if j > mid:
            cnt += j - mid
    if cnt < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)        
        
'''
    if M == 1 and mid == 1: #예외
        mid = 1
        break
    elif M == 1 and mid != 1: #예외
        mid = end - 1
        break
'''