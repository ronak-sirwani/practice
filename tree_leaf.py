class Node:
	def __init__(self):
		self.value= None
		self.left= None
		self.right= None

def leafNodes(root):
	if root==None:
		return

	if root.left==None and root.right==None:
		print(root.value,end="  ")

	if root.left:
		leafNodes(root.left)
	if root.right:
		leafNodes(root.right)

node1= Node()
node1.value= 1
node2= Node()
node2.value=2
node3= Node()
node3.value=3
node1.left= node2
node1.right= node3

node4= Node()
node4.value=4
node5= Node()
node5.value=5
node2.left= node4
node2.right= node5

node6= Node()
node6.value=6
node7= Node()
node7.value=7
node3.left= node6
node3.right= node7

leafNodes(node1)