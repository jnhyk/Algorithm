n = input()
A = 0
B = 0

if n[1] == "0":
    A = 10
    B = int(n[2:])
else:
    A = int(n[0])
    B = int(n[1:])
print(A+B)