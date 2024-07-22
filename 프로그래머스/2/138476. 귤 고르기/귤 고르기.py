from collections import Counter

def solution(k, tangerine):
    answer = 0
    t_cnt = list(Counter(tangerine).values())
    t_cnt.sort(reverse=True)
    for i in t_cnt:
        if k-i >= 0:
            answer += 1
            k -= i
        else:
            break
    if k > 0:
        answer += 1
        

    
    
    return answer