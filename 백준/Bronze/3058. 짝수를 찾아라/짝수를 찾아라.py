t = int(input())
for _ in range(t):
    num = list(map(int,input().split()))
    num.sort()
    s = 0
    m = -1
    for i in num:
        if i % 2 == 0:
            s += i
            if m == -1:
                m = i
    print(s, m)