from functools import reduce
def solution(sizes):
    for i in sizes:
        i[0], i[1] = max(i[0], i[1]), min(i[0], i[1])
    return reduce(lambda x,y : x*y, [max(i) for i in zip(*sizes)], 1)