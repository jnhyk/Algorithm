card, b, c = map(int, input().split())

b_x = card - b
c_x = card - c

result = 0
result += min(b, c) + min(b_x, c_x)
print(result)