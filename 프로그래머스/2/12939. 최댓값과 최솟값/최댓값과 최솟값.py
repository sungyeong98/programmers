def solution(s):
    s_list = list(map(int, s.split(" ")))
    return " ".join(list(map(str, [min(s_list), max(s_list)])))