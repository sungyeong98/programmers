from collections import Counter
def solution(s):
    result = 0
    zero_cnt = 0
    while s != "1":
        counter = Counter(s)
        cnt = counter["0"]
        n = len(s)
        temp = n - cnt
        s = bin(temp)[2:]
        result += 1
        zero_cnt += cnt
    return [result, zero_cnt]