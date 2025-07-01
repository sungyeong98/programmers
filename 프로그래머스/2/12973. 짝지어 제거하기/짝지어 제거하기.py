def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 1 if not stack else 0