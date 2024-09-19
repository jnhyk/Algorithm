n = int(input())
for _ in range(n):
    date = input()
    day = date[2:]
    day = int(day)
    if day > 90:
        n -= 1
print(n)