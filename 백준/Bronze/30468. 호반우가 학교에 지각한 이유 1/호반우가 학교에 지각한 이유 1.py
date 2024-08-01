a = list(map(int, input().split()))
b = (a[-1]*4) - sum(a[:4])
if b < 0:
    print(0)
else:
    print(b)