n = int(input())
win = []
d = 0
p = 0
for _ in range(n):
    win.append(input())
for i in win:
    if i == "D":
        d += 1
    else:
        p += 1
    if abs(d-p) == 2:
        break
print("%d:%d" % (d,p))