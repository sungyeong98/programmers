def solution(n):
    result = 2
    while n % result != 1:  result += 1
    return result