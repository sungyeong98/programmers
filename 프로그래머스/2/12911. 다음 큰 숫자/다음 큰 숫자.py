from collections import Counter
def solution(n):
    result = n + 1
    
    while True:
        if Counter(bin(result)[2:])["1"] == Counter(bin(n)[2:])["1"]:
            break
        result += 1
    return result