class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)

# create preorder traversal

def preorder(root):
    if root==None:
        return
    
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)

print("preorder :- ")
preorder(root)

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)
print()
print("inorder:- ")
inorder(root)

## now check BFS (Breath first search )- using this we can find height of the tree

from collections import deque

def BFS(root):
    count=0
    que=deque([])

    if root==None:
        return 0
    
    que.append(root)
    while len(que) !=0:
        count+=1
        level_size=len(que)

        for _ in range(level_size):
            e=que.popleft()
            if e.left != None:
                que.append(e.left)
            if e.right !=None:
                que.append(e.right)

    return count

print("height of Tree:- ",BFS(root))

## now try get max_height for the tree using recurision

def max_height_of_tree(root):
    if root==None:
        return 0
    left_height=max_height_of_tree(root.left)
    right_height=max_height_of_tree(root.right)
    return 1+max(left_height,right_height)
    
    

print("find max height of the tree:- ",max_height_of_tree(root))
