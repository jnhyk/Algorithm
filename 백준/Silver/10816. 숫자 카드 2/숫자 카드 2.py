from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

counters = Counter(n_list)

result = [counters[num] for num in m_list]

for r in result:
    print(r, end = " ")