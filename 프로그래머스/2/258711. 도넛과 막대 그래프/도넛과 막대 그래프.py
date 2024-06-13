
def find_new(dic):
    items = list(dic.items())
    values = list(dic.values())
    values = set([i for s in values for i in s])
    new = 0
    for i in items:
        if len(i[1]) > 1 and i[0] not in values:
            new = i[0]
    return new
    
def solution(edges):
    answer = [0,0,0,0]
    dic = {}
    for edge in edges:
        if edge[0] in dic:
            dic[edge[0]].append(edge[1])
        else:
            dic[edge[0]] = [edge[1]]
    answer[0] = find_new(dic)
    total = len(dic[answer[0]])
    k = set(dic.keys())
    v = list(dic.values())
    v_f = set([i for s in v for i in s])
    v = list(map(lambda x:len(x) > 1, v))
    answer[3] = v.count(True) - 1
    answer[2] = len(v_f - k)
    answer[1] = total - (answer[2] + answer[3])
    return answer