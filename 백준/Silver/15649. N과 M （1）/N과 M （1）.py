import itertools

n, m= map(int, input().split())
arr = [i for i in range(1,n+1)]
nPr = list(itertools.permutations(arr, m))
for i in range(len(nPr)):
    for j in range(m):
        print(nPr[i][j], end = " ")
    print()