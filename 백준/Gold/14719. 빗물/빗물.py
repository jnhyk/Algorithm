H, W = map(int, input().split())
block = list(map(int, input().split()))

rain = 0
for i in range(1, W - 1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    m = min(left_max, right_max)

    if block[i] < m:
        rain += m - block[i]

print(rain)