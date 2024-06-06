n, m, k = map(int, input().split())

m_day = n - (m*k)
if m_day < 0:
    m_day = 0
M_day = n - (m*(k-1)) - 1
if M_day < 0:
    M_day = 0
print(m_day, M_day)