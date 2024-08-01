a = "aeiouAEIOU"
while True:
    n = input()
    if n == "#":
        break
    count = 0
    for i in n:
        if i in a:
            count += 1
    print(count)