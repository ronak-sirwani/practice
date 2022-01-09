class Heap:
	def __init__(self):
		self.arr=[]

	def insert(self,item):
		if len(self.arr)==0:
			self.arr.append(item)
		else:
			self.arr.append(item)
			for i in range((len(self.arr)//2)-1,-1,-1):
				self.heapify(len(self.arr),i)

	def delete(self,item):
		n= len(self.arr)

		for i in range(n):
			if self.arr[i]==item:
				break

		temp= self.arr[i]
		self.arr[i]= self.arr[n-1]
		self.arr[n-1]=temp

		self.arr.remove(item)

		for i in  range((n//2)-1,-1,-1):
			self.heapify(len(self.arr),i)

	def heapify(self,n,i):
		
		largest= i

		l= 2*i + 1
		r= 2*i + 2

		if l<n and self.arr[largest] < self.arr[l]:
			largest= l
		if r<n and self.arr[largest] < self.arr[r]:
			largest= r

		if largest!=i:	
			temp= self.arr[i]
			self.arr[i]= self.arr[largest]
			self.arr[largest]=temp
				
			self.heapify(len(self.arr),largest)

h= Heap()
h.insert(1)
h.insert(4)
h.insert(10)
h.insert(3)
h.insert(2)
h.insert(6)
print(h.arr)
h.delete(10)
print(h.arr)