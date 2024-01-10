n = int(input())
dice = list(map(int, input().split()))
m = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
m.sort()
if n == 1:
    result = sum(dice) - max(dice)
else:
    result = (m[0]*(((n-2)**2) + (4*(n-1)*(n-2)))) + ((m[0]+m[1]) * (((n-1)*4) + ((n-2)*4))) + ((m[0]+m[1]+m[2])*4)
print(result)