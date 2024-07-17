n, k = map(int, input().split())
box = [[] for _ in range(2**k)]
ind = 0
for i in range(2**n):
    if (i//(2**k)) % 2 == 0:
        box[ind].append(str(i))
    else:
        box[2**k - ind - 1].append(str(i))
    ind = (ind+1) % (2**k)

str_box = list(map(lambda x: " ".join(x),box))
for i in str_box:
    print(i)