def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse = True)
    return sum([i * j for i, j in zip(a, b)])