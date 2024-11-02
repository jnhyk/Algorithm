def solution(sizes):
    answer = 0
    s1 = list(map(lambda x:sorted(x), sizes))
    m_x = 0
    m_y = 0
    for x,y in s1:
        if x > m_x:
            m_x = x
        if y > m_y:
            m_y = y
    
    answer = m_x * m_y
    return answer