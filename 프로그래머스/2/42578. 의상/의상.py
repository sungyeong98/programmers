from itertools import combinations
from collections import defaultdict
def solution(clothes):
    c = defaultdict(int)
    
    for _, tp in clothes:
        c[tp] += 1
    
    result = 1
    for i in c.values():
        result *= i + 1
    
    return result - 1