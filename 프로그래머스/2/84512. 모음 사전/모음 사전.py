from itertools import product
def solution(word):
    a = ['A', 'E', 'I', 'O', 'U']
    temp = []   # 모음 조합을 저장할 리스트
    for i in range(1, len(a)+1):
        for p in product(a, repeat=i):  # 모음 조합을 생성 및 저장
            temp.append("".join(p))
    return sorted(temp).index(word) + 1