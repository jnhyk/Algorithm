a = []
b = []
for i in range(6):
    if i < 4:
        a.append(int(input()))
    else:
        b.append(int(input()))
a.sort()
b.sort()
a.pop(0)
b.pop(0)
print(sum(a) + sum(b))