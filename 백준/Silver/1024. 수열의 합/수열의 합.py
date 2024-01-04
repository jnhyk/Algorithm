N,L = map(int,input().split())
error = True
while(L <= 100):
    sequence = L*(L-1)//2
    if (N - sequence) % L == 0 and (N - sequence) // L >= 0:
        start = (N-sequence) // L
        for i in range(start, start + L):
            print(i, end=" ")
        error = False
        break
    L += 1
if error:
    print(-1)