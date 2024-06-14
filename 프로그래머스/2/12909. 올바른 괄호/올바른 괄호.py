def solution(s):
    answer = True
    l = []
    for i in s:
        if i == "(":
            l.append(i)
        else:
            if l:
                l.pop()
            else:
                answer = False
                break
    if l:
        answer = False
                
    return answer