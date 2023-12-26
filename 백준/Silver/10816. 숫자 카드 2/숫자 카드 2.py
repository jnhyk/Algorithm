from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 첫 번째 리스트의 각 원소의 등장 횟수를 사전에 저장
n_counts = Counter(n_list)

# 결과 리스트 초기화
result = [n_counts[x] for x in m_list]

# 결과 출력
for r in result:
    print(r, end=" ")