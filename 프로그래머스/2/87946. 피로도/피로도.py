from itertools import permutations
def solution(k, dungeons):
    d = list(permutations(dungeons))
    answer = [0 for _ in range(len(d))]
    for i in range(len(d)):
        new_k = k
        for m, c in d[i]:
            if new_k >= m:
                answer[i] += 1
                new_k -= c
    return max(answer)