def lcm(a,b):
    for i in range(b,(a*b)+1):
        if i % a == 0 and i % b == 0:
            return i
def solution(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))
        print(arr)
    return arr[0]