def solution(brown, yellow):
    answer = []
    for i in range(1,int((brown+yellow) ** (1/2))+1):
        if (brown+yellow) % i == 0:
            y = i
            x = (brown+yellow) // i
            if yellow == x*y - (2*x + 2*y - 4):
                break
    answer = [x,y]
    return answer