n, m = map(int, input().split())
q = 0
for i in range(n):
    opinion = input()
    cnt = 0
    for i in opinion:
        if i =="O": 
            cnt += 1
    if cnt > m//2: 
        q += 1 
print(q)