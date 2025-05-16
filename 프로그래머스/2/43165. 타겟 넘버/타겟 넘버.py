from itertools import product
def solution(numbers, target):
    ops = [1, -1]
    result = 0
    for i in product(ops, repeat = len(numbers)):
        temp = 0
        for number, op in zip(numbers, i):
            temp += (number * op)
        if temp == target:
            result += 1
    return result