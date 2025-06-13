def solution(sequence):
    if len(sequence) == 1:  return abs(sequence[0])
    
    temp1 = [val if idx % 2 == 0 else -val for idx, val in enumerate(sequence)]
    temp2 = [val if idx % 2 == 1 else -val for idx, val in enumerate(sequence)]
    
    return max(find_max_value(temp1), find_max_value(temp2))

def find_max_value(seq):
    n = len(seq)
    result = [0] * n
    result[0] = seq[0]
    
    for idx, val in enumerate(seq):
        result[idx] = max(0, result[idx - 1]) + val
    
    return max(result)