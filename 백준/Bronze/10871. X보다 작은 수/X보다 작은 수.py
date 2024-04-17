n,x = input().split()
n, x = int(n), int(x) #10 5
l = list(map(int,input().split()))
for number in l:
    if number < x:
        print(number, end=" ")