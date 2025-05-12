def solution(s):
    temp = []
    for i in s:
        if not temp:
            temp.append(i)
        elif temp[-1]=='(' and i==')':
            temp.pop()
        else:
            temp.append(i)
    return True if not temp else False