while True:
    f, s = map(int, input().split())
    if f == 0 and s == 0:
        break
    if f > s:
        print("Yes")
    else:
        print("No")