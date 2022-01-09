class circularQueue:
	def __init__(self,_size):
		self.size= _size
		self.queue= [None]*size
		self.front=self.rear=-1

	def enqueue(self,item):
		# overflow condition
		if self.front== (self.rear+1)%self.size :
			print("queue full")

		# empty queue
		elif self.front==-1 and self.rear==-1:
			self.front=0
			self.rear=0
			self.queue[self.rear]= item

		else:
			self.rear= (self.rear+1) % self.size
			self.queue[self.rear]= item

	def dequeue(self):
		# underflow
		if self.front==-1:
			print("queue empty")

		# only 1 element i queue
		elif self.front==self.rear:
			temp= self.queue[self.front]
			self.front=-1
			self.rear=-1

		else:
			temp= self.queue[self.front]
			self.front= (self.front+1)%self.size
			return temp

	def display(self):
		print(self.queue)
		if self.front==-1:
			print("queue empty")

		elif self.rear >= self.front:
			for i in range(self.front,self.rear+1):
				print(self.queue[i],end=" ")
			print()

		else:
			for i in range(self.front,self.size):
				print(self.queue[i],end=" ")
			for i in range(0,self.rear+1):
				print(self.queue[i],end=" ")
			print()

size=int(input())
q= circularQueue(size)
q.enqueue(1)
q.display()
q.enqueue(2)
q.display()
q.enqueue(3)
q.display()
q.enqueue(4)
q.display()
q.dequeue()
q.display()
q.enqueue(1)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()