def P():
    if len(result) == n:
        print(' '.join(map(str, result)))
        return
    else:
        for i in L:
            if visited[i-1] == True:
                continue
            result.append(i)
            visited[i-1] = True
            P()
            result.pop()
            visited[i-1] = False


n = int(input())
L = [i for i in range(1,n+1)]

result = []
visited = [False for _ in range(n)]
P()