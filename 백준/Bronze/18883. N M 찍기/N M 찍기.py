n,m = map(int, input().split())
for i in range(1, n*m+1):#1~12
    if i % m ==0:
        print(i)
    else:
        print(i, end=" ")