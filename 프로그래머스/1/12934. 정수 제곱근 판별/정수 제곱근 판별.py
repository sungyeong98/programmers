import math
def solution(n):
    temp = math.sqrt(n)
    
    return (temp + 1) ** 2 if n % temp == 0 else -1