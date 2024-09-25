a, b = input().split()
a = int(a)
b = int(b)

if b+1 <= a:
    print(b + (b+1))
else:
    print(a + (a-1))