def solution(n):
    answer = 0
    for i in range(1, n//2+1):
        sum_v = 0
        for j in range(i,n):
            sum_v += j
            if sum_v == n:
                answer += 1
                break
            elif sum_v > n:
                break
            
    return answer + 1