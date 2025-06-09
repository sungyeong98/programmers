def solution(a, b):
    return sum([i for i in range(min(a, b), max(a, b) + 1)]) if a != b else a