n = int(input())
a = 100
b = 100
for _ in range(n):
    a_dice, b_dice = map(int,input().split())
    if a_dice == b_dice:
        continue
    elif a_dice < b_dice:
        a -= b_dice
    else:
        b -= a_dice
print(a)
print(b)