def solution(s):
    answer = ''
    gh = len(s)
    if gh % 2 == 0:
        m = gh // 2 - 1
        answer = s[m:m+2]
    else:
        m = gh // 2
        answer = s[m]
    return answer

