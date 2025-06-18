from itertools import permutations
def solution(babbling):
    word_list = ["aya", "ye", "woo", "ma"]
    temp = []
    for i in range(1, 5):
        for p in permutations(word_list, i):
            temp.append("".join(p))
    result = 0
    for i in babbling:
        if i in temp:
            result += 1
    return result