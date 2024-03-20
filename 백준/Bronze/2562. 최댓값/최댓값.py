m = 0 
k = 0 
for i in range(1,10): 
    n = int(input()) 
    if m < n: 
        m = n
        k = i
print(m)
print(k)