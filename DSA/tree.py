# creating tree

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

## Part of DFS (Depth first search)
def preorder(root):
    if root==None:
        return 
    
    print(root.value)
    preorder(root.left)
    preorder(root.right)

print("Preorder :- ")
preorder(root)


def inorder(root):
    if root==None:
        return
    
    inorder(root.left)
    print(root.value)
    inorder(root.right)

print("Inorder :- ")
inorder(root)


## Part of BFS (Breath First Search)

from collections import deque

que=deque([])

print(que)
que.append(10)
que.append(120)
que.append(130)
que.append(110)
print(que)
que.popleft()
print(que)
que.append(110)
que.popleft()
print(que)

def breate_first_search(root):
    result=[]
    que=deque([])
    que.append(root)
    while len(que)!=0:
        e=que.popleft()
        result.append(e.value)
        if e.left != None:
            que.append(e.left)
        if e.right != None:
            que.append(e.right)
    
    return result

print("breath first search:- ")
print(breate_first_search(root))


