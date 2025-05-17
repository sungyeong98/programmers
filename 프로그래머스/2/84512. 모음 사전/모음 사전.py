from itertools import product
def solution(word):
    a = ['A', 'E', 'I', 'O', 'U']
    temp = []
    for i in range(1, len(a)+1):
        for p in product(a, repeat=i):
            temp.append("".join(p))
    return sorted(temp).index(word) + 1