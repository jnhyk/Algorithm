N, X = map(int, input().split())
A = list(map(int, input().split()))
m = A[0]*X + A[1]*X
for i in range(1,N-1):
    if (A[i]*X + A[i+1]*X) < m:
        m = A[i]*X + A[i+1]*X

print(m)