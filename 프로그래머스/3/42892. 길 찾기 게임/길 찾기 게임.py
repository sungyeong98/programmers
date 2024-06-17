import sys
sys.setrecursionlimit(10**6)
class tree:
    def __init__(self):
        self.parent=None
        self.left=None
        self.right=None
        self.data=None
        self.index=None
def pre(root,temp):
    if root==None:
        return temp
    temp.append(root.index)
    pre(root.left,temp)
    pre(root.right,temp)
    return temp
def post(root,temp):
    if root==None:
        return temp
    post(root.left,temp)
    post(root.right,temp)
    temp.append(root.index)
    return temp
def solution(n):
    root=None
    for i in range(len(n)):
        n[i].append(i+1)
    n.sort(key=lambda x:-x[1])
    for idx,node in enumerate(n):
        nt=tree()
        nt.index=node[2]
        nt.data=node
        if root==None:
            root=nt
        else:
            temp=root
            while True:
                if temp.data[0]<nt.data[0]:
                    if temp.right==None:
                        temp.right=nt
                        nt.parent=temp
                        break
                    else:
                        temp=temp.right
                else:
                    if temp.left==None:
                        temp.left=nt
                        nt.parent=temp
                        break
                    else:
                        temp=temp.left
    answer=[pre(root,[]),post(root,[])]
    return answer