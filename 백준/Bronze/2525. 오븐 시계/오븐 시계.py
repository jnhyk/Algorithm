h, m = map(int, input().split())
n = int(input())

if (n+m) < 60:
    m += n
else:
    h += (n+m) // 60
    m = (n+m) % 60
h %= 24
print(h,m)