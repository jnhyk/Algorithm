m,M = map(int,input().split())
L = [False for _ in range(m,M+1)]
count = M-m+1
for i in range(2,int(M**(1/2))+1):
    square = i**2
    for j in range(((m-1)//square+1)*square,M+1,square):
        if not L[j-m]:
            L[j-m] = True
            count -= 1
print(count)
