l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

k = a//c
m = b//d

if a%c != 0:
    k += 1

if b%d != 0:
    m += 1

print(l - max(k,m))