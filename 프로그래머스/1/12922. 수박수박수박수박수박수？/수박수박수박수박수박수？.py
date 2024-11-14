def solution(n):
    answer = n // 2 * "수박"
    if n % 2 == 1:
        answer += "수"
    return answer