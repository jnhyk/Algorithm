def solution(num_list):
    e = sum(num_list[i] for i in range(0,len(num_list),2))
    o = sum(num_list[i] for i in range(1,len(num_list),2))
    return max(e,o)

    