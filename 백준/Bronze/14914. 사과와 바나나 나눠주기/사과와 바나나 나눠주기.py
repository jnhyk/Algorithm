a,b = map(int, input().split())
l = []
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        l.append(i)

for i in l:
    print(i, a//i, b//i)

        






