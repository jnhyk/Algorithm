a = [0,0]
def trans(s):
    if s == "1":
        return
    l1 = len(s)
    s = s.replace("0", "")
    l2 = len(s)
    a[1] += l1 - l2
    s = bin(l2)[2:]
    a[0] += 1
    trans(s)
    
def solution(s):
    trans(s)
    answer = a
    return answer