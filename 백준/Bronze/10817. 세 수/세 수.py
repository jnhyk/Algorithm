a,b,c = map(int, input().split())

if (c <= a and a <= b) or (b <= a and a <= c):
    print(a)
elif (a <= b and b <= c) or (c <= b and b <= a):
    print(b)
else:
    print(c)