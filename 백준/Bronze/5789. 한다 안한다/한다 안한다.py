t = int(input())
for i in range(t):
    s = input()
    s = list(s)
    k = len(s)//2 - 1
    if s[k] == s[k+1]:
        print("Do-it")
    else:
        print("Do-it-Not")