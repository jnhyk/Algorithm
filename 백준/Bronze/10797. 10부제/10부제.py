s = 0
n = int(input())
a,b,c,d,e = map(int, input().split())
if n == a:
    s += 1
if n == b:
    s += 1
if n == c:
    s += 1
if n == d:
    s += 1
if n == e:
    s += 1
print(s)
