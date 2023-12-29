n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
    xy[i].reverse()
xy.sort()
for i in range(n):
    xy[i].reverse()
for i in range(n):
    print(xy[i][0], xy[i][1])