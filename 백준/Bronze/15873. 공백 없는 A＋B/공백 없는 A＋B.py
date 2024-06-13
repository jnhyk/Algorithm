n = input() #"910" "101"
A = 0
B = 0
if len(n) == 2: #A = int("3") B = int("7")
    A,B = int(n[0]), int(n[1])
elif len(n) == 3:
    if n[1] == "0":
        A, B = 10,int(n[2])
    else:
        A, B = int(n[0]), 10
else:
    A, B = 10,10
print(A+B)