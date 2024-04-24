N = int(input())
num = int(input())
s = 0
for i in range(N):
    s += num % 10
    num //= 10
print(s)