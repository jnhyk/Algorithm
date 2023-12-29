from collections import deque
T = int(input())
for _ in range(T):
    count = 0
    p = input()
    n = int(input())
    L = input()
    if p.count('D') > n:
        print("error")
        continue
    if n == 0:
        L = deque()
    else:
        L = deque(L[1:-1].split(','))
    for i in range(len(p)):
        if p[i] == 'R':
            count += 1
        elif p[i] == 'D':
            if count%2 == 0:
                L.popleft()
            else:
                L.pop()
    if count%2 == 1:
        L.reverse()
    result = ','.join(L)
    print(f'[{result}]')