def solution(s):
    answer = ''
    l = list(map(int,s.split()))
    l.sort()
    answer = str(l[0]) + " " + str(l[-1])
    return answer