import math
from itertools import permutations
def solution(numbers):
    temp = set()
    for size in range(1, len(numbers) + 1):
        for p in permutations(list(numbers), size):
            temp.add(int("".join(p)))
    result = 0
    for num in temp:
        if num < 2:
            continue
        flag = True
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                flag = False
                break
        if flag:
            result += 1
    
    return result