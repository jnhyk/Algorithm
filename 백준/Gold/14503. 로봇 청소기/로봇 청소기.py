n,m = map(int, input().split())
r,c,d = map(int, input().split())
n_list = []
end = 0
result = 0
for _ in range(n):
    n_list.append(list(map(int, input().split())))
while(end == 0):
    if n_list[r][c] == 0:
        n_list[r][c] = 2
        result += 1
    if n_list[r - 1][c] != 0 and n_list[r + 1][c] != 0 and n_list[r][c - 1] != 0 and n_list[r][c + 1] != 0:
        if d == 0:
            if n_list[r + 1][c] == 1:
                end = 1
            else:
                r += 1
        elif d == 1:
            if n_list[r][c - 1] == 1:
                end = 1
            else:
                c -= 1
        elif d == 2:
            if n_list[r - 1][c] == 1:
                end = 1
            else:
                r -= 1
        else:
            if n_list[r][c + 1] == 1:
                end = 1
            else:
                c += 1
    else:
        d = (d + 3)%4
        if d == 0:
            if n_list[r - 1][c] == 0 :
                r -= 1
        elif d == 1:
            if n_list[r][c + 1] == 0:
                c += 1
        elif d == 2:
            if n_list[r + 1][c] == 0:
                r += 1
        else:
            if n_list[r][c - 1] == 0:
                c -= 1
print(result)
