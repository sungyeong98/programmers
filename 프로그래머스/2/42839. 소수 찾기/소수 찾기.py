import math
from itertools import permutations
def solution(numbers):
    temp = set()    # 숫자 조합을 저장할 변수
    for size in range(1, len(numbers) + 1):     # 1부터 numbers 길이까지
        for p in permutations(list(numbers), size):     # 순열을 사용하여 숫자 조합
            temp.add(int("".join(p)))
    result = 0      # 소수 갯수 저장 변수
    for num in temp:    # temp에 저장된 숫자 조합을 순회
        if num < 2:     # 2보다 작으면 패스
            continue
        flag = True     # 현재 숫자가 소수인지 확인하기 위한 boolean
        for i in range(2, int(math.sqrt(num) + 1)):     # 루트(num)까지 순회하면서 약수가 있는지 확인
            if num % i == 0:    # 약수가 존재하면 flag = False로 변경 및 종료
                flag = False
                break
        if flag:    # 소수라고 판별됐으면 result에 +1
            result += 1
    
    return result