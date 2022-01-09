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

	def bfs(self,start):
		visited=[]
		q= []
		q.append(start)

		while len(q)>0:
			front= q[0]

			q.pop(0)
			visited.append(front)

			for i in self.graph[front]:
				if (i not in visited) and (i not in q):
					q.append(i)

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
g.addEdge(3,4)
g.addEdge(1,5)
g.addEdge(0,5)
g.addEdge(6,5)
# g.displayGraph()
# g.deleteEdge(2,0)
g.displayGraph()
print("BFS traversal of graph: ",g.bfs(0))