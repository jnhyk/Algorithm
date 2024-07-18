n = int(input()) 
result = 5
plus = 7
for i in range(n-1):
    result += plus
    plus += 3
    result %= 45678 
print(result)