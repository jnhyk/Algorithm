from itertools import permutations
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    result = True
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            result = False
            break
    return result
        
def solution(numbers):
    answer = 0
    numbers = list(map(int, list(numbers)))
    all_numbers = set()

    for r in range(1, len(numbers) + 1):
        for perm in permutations(numbers, r):
            num = int("".join(map(str, perm)))
            all_numbers.add(num)
    all_numbers = list(all_numbers)
    answer = list(map(isPrime, all_numbers))
    return answer.count(True)