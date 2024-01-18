n, m = map(int,input().split())
party = []
count = 0
know_peaple= list(map(int, input().split()[1:]))

for _ in range(m):
    party.append(list(map(int, input().split()[1:])))
sorted_party = sorted(party, key=lambda x: set(know_peaple) & set(x), reverse=True)
for i in range(m):
    if set(know_peaple) & set(sorted_party[i]):
        count+=1
        know_peaple = set(know_peaple) | set(sorted_party[i])
        sorted_party = sorted(sorted_party, key=lambda x: set(know_peaple) & set(x), reverse=True)
print(m-count)