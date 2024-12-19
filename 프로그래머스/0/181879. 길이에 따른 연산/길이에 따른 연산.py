def solution(num_list):
    answer = 0
    if len(num_list) <= 10:
        answer = 1
        for i in num_list:
            answer *= i
    else:
        for i in num_list:
            answer += i
            
    return answer