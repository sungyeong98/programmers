from collections import Counter
def solution(nums):
    n = len(nums)//2
    length = len(set(nums))
    return min(n, length)