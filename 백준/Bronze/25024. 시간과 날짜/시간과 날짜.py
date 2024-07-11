t = int(input())
for _ in range(t):
    time = "Yes" #시간이 되나!
    day = "Yes" # 날짜가 되나!
    x, y = map(int, input().split())
    if x > 23 or y > 59:
        time = "No"
        day = "No"
    elif (x < 1 or x > 12) or (y < 1 or y > 31):
        day = "No"
    else:
        if (x in [4,6,9,11] and y > 30) or (x == 2 and y > 29):
            day = "No"
    print(time, day)
