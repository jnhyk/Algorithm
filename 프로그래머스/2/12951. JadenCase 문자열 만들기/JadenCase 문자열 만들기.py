def solution(s):
    s_list = list(s)
    
    for i in range(len(s_list)):
        if i == 0 or s_list[i-1] == " ":
            s_list[i] = s_list[i].upper()
        else:
            s_list[i] = s_list[i].lower()
    
    answer = ''.join(s_list)
    return answer