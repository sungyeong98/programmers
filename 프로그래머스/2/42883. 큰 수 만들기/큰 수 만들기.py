def solution(number, k):
    temp = []   # 스택 역할
    
    # 매커니즘 : 앞에서부터 순회하면서 값을 스택에 넣고, 다음 값과 비교하여 작은 값은 삭제하는 식으로 큰 수를 생성
    #           만약 모든 숫자를 전부 순회했지만 k의 값이 남아 있다면, 맨 뒤에서부터 값을 삭제
    #           (앞에 있는 숫자들이 클 것이라 판단)
    for num in number:
        # temp에 값이 들어있고, temp의 마지막 값이 현재 값보다 작고, k가 0보다 크다면
        while temp and temp[-1] < num and k > 0:
            temp.pop()  # temp에 들어있는 값을 제거
            k -= 1      # k--
        temp.append(num)
    
    return "".join(temp) if k == 0 else "".join(temp[:-k])