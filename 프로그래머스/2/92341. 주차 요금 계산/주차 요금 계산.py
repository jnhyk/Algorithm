import math
def trans_t(t):
    h,m = map(int,t.split(":"))
    m += h*60
    return m
    
def no_out(l):
    if len(l) % 2 == 1:
        l.append(1439)
    return l
def solution(fees, records):
    answer = []
    dic = {}
    records = list(map(lambda x:x.split(), records))
    for i in records:
        if i[1] not in dic:
            dic[i[1]] = [trans_t(i[0])]
        else:
            dic[i[1]].append(trans_t(i[0]))
    dic = {key: no_out(value) for key, value in dic.items()}
    for k,v in dic.items():
        n_v = []
        for i in range(0,len(v),2):
            n_v.append(v[i+1] - v[i])
        dic[k] = sum(n_v)
    sorted_items = sorted(dic.items())
    sorted_values = [value for key, value in sorted_items]
    answer = list(map(lambda x: fees[1] + math.ceil((x - fees[0])/fees[2])*fees[3] if x > fees[0] else fees[1], sorted_values))
    
    
    return answer