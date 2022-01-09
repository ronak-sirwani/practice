class Node:
    def __init__(self,val) -> None:
        self.data= val
        self.left= None
        self.right= None

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def insertNode(lst,i,n):
    if i<n:
        root= Node(lst[i])
        root.left= insertNode(lst,(i*2)+1,n)
        root.right= insertNode(lst,(i*2)+2,n)
    else:
        return None
    
    return root

n= int(input("Enter no. : "))
lst= list(map(int,input().split()))
root= insertNode(lst,0,n)

print("preorder: ")
preorder(root)

print("\ninorder: ")
inorder(root)

print("\npostorder: ")
postorder(root)
    