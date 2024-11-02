def solution(sizes):
    answer = 0
    s1 = list(map(lambda x:sorted(x), sizes))
    m_x = 0
    m_y = 0
    for x,y in s1:
        m_x = max(m_x, x)
        m_y = max(m_y, y)
    answer = m_x * m_y
    return answer