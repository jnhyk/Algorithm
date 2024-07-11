t = int(input())
for _ in range(t):
    time = "Yes"
    day = "Yes"
    x, y = map(int, input().split())
    if x > 23 or y > 59:
        time = "No"
        day = "No"
    elif (x < 1 or x > 12) or (y < 1 or y > 31):
        day = "No"
    else:
        if ((x == 4 or x == 6 or x == 9 or x == 11) and y > 30) or (x == 2 and y > 29):
            day = "No"
    print(time, day)
