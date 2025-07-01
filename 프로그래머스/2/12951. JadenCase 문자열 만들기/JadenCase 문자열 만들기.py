def solution(s):
    s_list = s.split(" ")
    return " ".join([i[:1].upper() + i[1:].lower() for i in s_list])