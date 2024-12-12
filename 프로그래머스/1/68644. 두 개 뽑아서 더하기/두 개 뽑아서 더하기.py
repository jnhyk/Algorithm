def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
#난이도 : 어려움 아마도 엄청 어려움
#이 문제를 푸는데에는 
#1. 이중 포문
#2. list -> set -> list -> sort
