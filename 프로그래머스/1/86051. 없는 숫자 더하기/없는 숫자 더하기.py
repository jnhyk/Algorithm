#1
def solution(numbers):
    answer = -1
    l = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        l.remove(i)
    answer = sum(l)
    return answer