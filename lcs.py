def lengthLCS(x,y,m,n,l):
	if m==0 or n==0:
		return l

	if x[m-1]==y[n-1]:
		l= lengthLCS(x,y,m-1,n-1,l+1)
		return l
	else:
		return max(l,lengthLCS(x,y,m-1,n,0),lengthLCS(x,y,m,n-1,0))

x= input()
m= len(x)
y= input()
n= len(y)
dp= [[-1 for i in range(n+1)] for j in range(m+1)]
l= 0
temp=lengthLCS(x,y,m,n,l)
print(temp)