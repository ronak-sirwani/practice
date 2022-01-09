def lcs(x,y,m,n):
	global dp

	for i in range(n+1):
		dp[0][i]=0
	for i in range(m+1):
		dp[i][0]=0

	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i-1]==y[j-1]:
				dp[i][j]= 1+dp[i-1][j-1]
			else:
				dp[i][j]= max(dp[i-1][j],dp[i][j-1])

def printlcs(x,y,m,n,s=""):
	global dp
	global lst

	i=m
	j=n

	while i>0 and j>0:
		if x[i-1]==y[j-1]:
			s+= x[i-1]
			i-=1
			j-=1
		elif dp[i][j-1] == dp[i-1][j]:
			lst.append(printlcs(x,y,i-1,j,s))
			lst.append(printlcs(x,y,i,j-1,s))
			break
		elif dp[i][j-1] > dp[i-1][j]:
			j-=1
		else:
			i-=1

	return s[::-1]

x= input()
m= len(x)
y= input()
n= len(y)
dp= [[-1 for i in range(n+1)] for j in range(m+1)]
lst=[]
lcs(x,y,m,n)
res= dp[m][n]
temp= printlcs(x,y,m,n)
lst.append(temp)
lst2=[]
for i in lst:
	if i not in lst2:
		if len(i)==res:
			lst2.append(i)
lst2.sort()
print(" ".join(lst2))