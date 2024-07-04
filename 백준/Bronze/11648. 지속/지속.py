n = input()
count = 0
while(len(n)>=2):
    temp = 1
    for i in n:
        temp *= int(i)
    count += 1
    n = str(temp)
print(count)