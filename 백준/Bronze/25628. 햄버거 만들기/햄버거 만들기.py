a,b = map(int, input().split())
if a % 2 == 1:
    a = a - 1
a = a // 2
if a > b:
    print(b)
else:
    print(a)
