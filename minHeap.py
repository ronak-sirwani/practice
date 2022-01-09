class Heap:
	def __init__(self):
		self.arr= []

	def insert(self,item):
		if len(self.arr) == 0:
			self.arr.append(item)
		else:
			self.arr.append(item)
			for i in range(len(self.arr)//2-1,-1,-1):
				self.heapify(len(self.arr),i)

	def delete(self,item):
		n= len(self.arr)

		for i in range(n):
			if self.arr[i]==item:
				break

		self.arr[n-1],self.arr[i]= self.arr[i],self.arr[n-1]
		self.arr.remove(item)

		for i in range(len(self.arr)//2 -1, -1,-1):
			self.heapify(len(self.arr),i)


	def heapify(self,n,i):	
		smallest= i

		left= 2*i + 1
		right= 2*i + 2

		if left<n and self.arr[left] < self.arr[smallest]:
			smallest= left
		if right<n and self.arr[right] < self.arr[smallest]:
			smallest= right

		if smallest!=i:
			self.arr[i],self.arr[smallest]= self.arr[smallest],self.arr[i]
			self.heapify(len(self.arr),smallest)

h= Heap()
h.insert(6)
print(h.arr)
h.insert(2)
print(h.arr)
h.insert(3)
print(h.arr)
h.insert(10)
print(h.arr)
h.insert(4)
print(h.arr)
h.insert(1)
print(h.arr)
h.delete(4)
print(h.arr)