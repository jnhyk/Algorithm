T = int(input())
for _ in range(T):
    l,n = map(int,input().split())
    loc = []
    m = 0
    M = 0
    for _ in range(n):
        num = (int(input()))
        loc.append(num)
        if m < min(l - num, num):
            m = min(l - num, num)
        if M < max(l - num, num):
            M = max(l - num, num)
    print(m, M)

