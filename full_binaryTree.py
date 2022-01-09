class Node:
    def __init__(self,val) -> None:
        self.data= val 
        self.left= None
        self.right= None

def isFullBinaryTree(root):
    if root is None:
        return True
    
    if root.left==None and root.right==None:
        return True
    
    if root.left!=None and root.right!=None:
        return (isFullBinaryTree(root.left) and isFullBinaryTree(root.right))

    return False

root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

print(isFullBinaryTree(root))