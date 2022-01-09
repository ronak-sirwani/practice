class Node:
	def __init__(self):
		self.value= None
		self.left= None
		self.right= None

def level_order(root):
	if root==None:
		return 

	q= []
	q.append(root)
	while len(q)>0:
		curr= q[0]
		q.pop(0)
		print(curr.value, end=" ")

		if curr.left:
			q.append(curr.left)
		if curr.right:
			q.append(curr.right)

def level_wise(root):
	if root==None:
		return 

	q= []
	q.append(root)
	i=1
	while len(q)>0:
		temp= len(q)
		print("Level : ",i)
		while temp>0:
			curr= q[0]
			q.pop(0)
			print(curr.value, end=" ")

			if curr.left:
				q.append(curr.left)
			if curr.right:
				q.append(curr.right)

			temp-=1
		print()
		i+=1

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

print("Level order traversal: ")
level_order(node1)
print("\nLevel wise elements: ")
level_wise(node1)