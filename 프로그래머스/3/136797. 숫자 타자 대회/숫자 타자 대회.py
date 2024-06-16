cost={(1, 0): 7, (1, 1): 1, (1, 2): 2, (1, 3): 4, (1, 4): 2, (1, 5): 3, (1, 6): 5, (1, 7): 4, (1, 8): 5, (1, 9): 6, 
      (2, 0): 6, (2, 1): 2, (2, 2): 1, (2, 3): 2, (2, 4): 3, (2, 5): 2, (2, 6): 3, (2, 7): 5, (2, 8): 4, (2, 9): 5, 
      (3, 0): 7, (3, 1): 4, (3, 2): 2, (3, 3): 1, (3, 4): 5, (3, 5): 3, (3, 6): 2, (3, 7): 6, (3, 8): 5, (3, 9): 4, 
      (4, 0): 5, (4, 1): 2, (4, 2): 3, (4, 3): 5, (4, 4): 1, (4, 5): 2, (4, 6): 4, (4, 7): 2, (4, 8): 3, (4, 9): 5,  
      (5, 0): 4, (5, 1): 3, (5, 2): 2, (5, 3): 3, (5, 4): 2, (5, 5): 1, (5, 6): 2, (5, 7): 3, (5, 8): 2, (5, 9): 3, 
      (6, 0): 5, (6, 1): 5, (6, 2): 3, (6, 3): 2, (6, 4): 4, (6, 5): 2, (6, 6): 1, (6, 7): 5, (6, 8): 3, (6, 9): 2, 
      (7, 0): 3, (7, 1): 4, (7, 2): 5, (7, 3): 6, (7, 4): 2, (7, 5): 3, (7, 6): 5, (7, 7): 1, (7, 8): 2, (7, 9): 4, 
      (8, 0): 2, (8, 1): 5, (8, 2): 4, (8, 3): 5, (8, 4): 3, (8, 5): 2, (8, 6): 3, (8, 7): 2, (8, 8): 1, (8, 9): 2, 
      (9, 0): 3, (9, 1): 6, (9, 2): 5, (9, 3): 4, (9, 4): 5, (9, 5): 3, (9, 6): 2, (9, 7): 4, (9, 8): 2, (9, 9): 1,
      (0, 0): 1, (0, 1): 7, (0, 2): 6, (0, 3): 7, (0, 4): 5, (0, 5): 4, (0, 6): 5, (0, 7): 3, (0, 8): 2, (0, 9): 3}
from collections import deque
def solution(numbers):
    q,dict=deque(),{}
    dict[(4,6)]=0
    for str_num in numbers:
        num=int(str_num)
        new_dict={}
        for left,right in dict.keys():
            q.append((left,right,dict[(left,right)]))
        while q:
            cur_left,cur_right,cur_cost=q.popleft()
            left_cost=cost[(cur_left,num)]
            right_cost=cost[(cur_right,num)]
            if cur_left==num:
                if (num,cur_right) not in new_dict.keys() or new_dict[(num,cur_right)]>cur_cost+1:
                    new_dict[(num,cur_right)]=cur_cost+1
            elif cur_right==num:
                if (cur_left,num) not in new_dict.keys() or new_dict[(cur_left,num)]>cur_cost+1:
                    new_dict[(cur_left,num)]=cur_cost+1
            else:
                if (num,cur_right) not in new_dict.keys() or new_dict[(num,cur_right)]>cur_cost+left_cost:
                    new_dict[(num,cur_right)]=cur_cost+left_cost
                if (cur_left,num) not in new_dict.keys() or new_dict[(cur_left,num)]>cur_cost+right_cost:
                    new_dict[(cur_left,num)]=cur_cost+right_cost
        dict=new_dict
    return min(dict.values())