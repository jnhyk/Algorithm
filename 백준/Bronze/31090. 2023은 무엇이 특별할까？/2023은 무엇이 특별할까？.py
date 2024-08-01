t = int(input())
for _ in range(t):
    year = int(input())
    next_year = year + 1
    n = year % 100

    if next_year % n == 0:
        print("Good")
    else:
        print("Bye")