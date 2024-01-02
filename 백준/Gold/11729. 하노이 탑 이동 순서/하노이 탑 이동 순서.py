def hanoi(N):
    if N == 1:
        return [1,3]
    H = hanoi(N-1)
    for i in range(len(H)):
        if H[i] == 2:
            H[i] = 3
        elif H[i] == 3:
            H[i] = 2
    L = H + [1,3]
    for i in range(len(H)):
        if H[i] == 1:
            H[i] = 2
        elif H[i] == 2:
            H[i] = 3
        else:
            H[i] = 1
    L += H
    return L

N = int(input())
result = hanoi(N)
print(len(result)//2)
for i in range(0,len(result),2):
    print(result[i], result[i+1])

