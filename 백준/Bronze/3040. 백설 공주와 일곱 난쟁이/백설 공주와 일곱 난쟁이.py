n_list = []
sum = -100
for _ in range(9):
    n = int(input())
    n_list.append(n)
    sum += n

for i in n_list:
    if (sum-i) in n_list and sum-i != i:
        n_list.remove(sum-i)
        n_list.remove(i)
        break
    else:
        continue
for i in n_list:
    print(i)

