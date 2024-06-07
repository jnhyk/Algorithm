def rem(x,a):
    x.remove(a)
    return x
def solution(s):
    answer = []
    s = s[2:len(s)-2]
    s = s.split("},{")
    s.sort(key=len)
    s.reverse()
    s = list(map(lambda x: x.split(","),s))
    k = len(s)
    for _ in range(k):
        a = s.pop()[0]
        answer.append(int(a))
        s = list(map(lambda x: rem(x,a),s))
    return answer