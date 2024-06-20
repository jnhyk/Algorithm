t = int(input())
for _ in range(t):
    happy = 0
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    for i in range(n):
        happy += candy[i]//k
    print(happy)