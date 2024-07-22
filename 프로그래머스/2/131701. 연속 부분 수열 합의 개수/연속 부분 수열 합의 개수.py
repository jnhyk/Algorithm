def solution(elements):
    answer = 0
    pre = [[0 for _ in range(len(elements))] for _ in range(len(elements))]
    for i in range(len(elements)):
        pre[i][i] = elements[i]
        for j in range(i+1,len(elements)+i):
            if j >= len(elements):
                j -= len(elements)
            pre[i][j] = pre[i][j-1] + elements[j]
    flattened_list = [element for row in pre for element in row]
    answer = len(set(flattened_list))
    return answer
