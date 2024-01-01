def star(n):
    if n ==3:
        L.append(['  *   ',' * *  ','***** '])
        return L
    
    S = star(n//2)
    L.append(list(map(lambda x: x * 2,S[-1])))
    L[-2] = list(map(lambda x: ' '*(n//2)+x+' '*(n//2), L[-2]))
    L[0] += L[1]
    L.pop()
    return L
    


n = int(input())
L = []
print('\n'.join(sum(star(n),[])))