def solution(numbers):
    result = "".join(sorted(list(map(str, numbers)), key=lambda x:x*4, reverse=True))
    return result if int(result)!=0 else "0"
        