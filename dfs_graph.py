from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph= defaultdict(lambda: list())

	def addEdge(self,u,v):
		if v not in self.graph[u]:
			self.graph[u].append(v)
			self.graph[v].append(u)

	def deleteEdge(self,u,v):	
		self.graph[u].remove(v)
		self.graph[v].remove(u)

	def displayGraph(self):
		for i in self.graph:
			print(i,self.graph[i])

	def dfs(self,start,visited= None):
		if visited==None:
			visited=[]

		visited.append(start)

		for i in self.graph[start]:
			if i not in visited:
				self.dfs(i,visited)

		return visited

	def dfs_iterative(self,start):
		visited=[]
		stk=[]
		stk.append(start)

		while len(stk)>0:
			top= stk[len(stk)-1]

			visited.append(top)
			stk.pop()

			for i in self.graph[top][::-1]:
				if (i not in visited) and (i not in stk):
					stk.append(i)

		return visited

g = Graph()
g.addEdge(0, 1)
# g.displayGraph()
g.addEdge(0, 2)
# g.displayGraph()
g.addEdge(1, 2)
# g.displayGraph()
g.addEdge(2, 0)
# g.displayGraph()
g.addEdge(2, 3)
# g.displayGraph()
# g.deleteEdge(2,0)
g.displayGraph()

print("Recursive DFS traversal of graph : ",g.dfs(2))
print("Iterative DFS traversal of graph : ",g.dfs_iterative(2))