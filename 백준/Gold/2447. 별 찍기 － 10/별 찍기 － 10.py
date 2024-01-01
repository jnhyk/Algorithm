def star(n):
    if n ==3:
        return ['***','* *','***']
    S = star(n//3)
    L = []
    L.append(list(map(lambda x: x * 3,S)))
    L.append(list(map(lambda x: x +' '*(n//3)+x,S)))
    L.append(list(map(lambda x: x * 3,S)))
    L = L[0] + L[1] + L[2]
    return L
    


n = int(input())
print('\n'.join(star(n)))