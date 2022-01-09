# recursive approach

# def maxValue(wt,val,W,n):
#     if n==0 or W==0:
#         return 0
    
#     if wt[n-1] <= W:
#         return max(val[n-1]+maxValue(wt,val,W-wt[n-1],n-1),maxValue(wt,val,W,n-1))
#     else:
#     	return maxValue(wt,val,W,n-1)



# memoization approach    

def maxValue(wt,val,W,n):
	if n==0 or W==0:
		return 0

	if dp[n][W]!=-1:
		return dp[n][W]

	if wt[n-1] <= W:
		dp[n][W]= max(val[n-1]+maxValue(wt,val,W-wt[n-1],n-1),maxValue(wt,val,W,n-1))
		return dp[n][W]
	else:
		dp[n][W]= maxValue(wt,val,W,n-1)
		return dp[n][W]


# bottom-up approach

# def maxValue(wt,val,W,n):
# 	# initialization
# 	for i in range(W+1):
# 		dp[0][i]= 0
# 	for i in range(n+1):
# 		dp[i][0]= 0

# 	# choice diagram
# 	for i in range(1,n+1):
# 		for j in range(1,W+1):
# 			if wt[i-1] <= j:
# 				dp[i][j]= max(val[i-1] + dp[i-1][j-wt[i-1]] , dp[i-1][j])
# 			else:
# 				dp[i][j]= dp[i-1][j]

wt= list(map(int,input().split()))
val= list(map(int,input().split()))
W= int(input())
n= len(wt)
dp= [[-1 for i in range(W+1)] for j in range(n+1)]
maxValue(wt,val,W,n)
print(dp[n][W])