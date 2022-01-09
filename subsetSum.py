class Solution:
    def __init__(self):
        self.dp= [[-1 for i in range(sum+1)] for j in range(N+1)]
    
    def isSubsetSum (self, N, arr, sum):
        # code here 
        if sum==0:
            return 1
        if N==0:
            return 0
        if self.dp[N][sum] != -1:
            return self.dp[N][sum]
        
        if arr[N-1] <= sum:
            self.dp[N][sum]= self.isSubsetSum(N-1,arr,sum-arr[N-1]) or self.isSubsetSum(N-1,arr,sum)
            return self.dp[N][sum]
        else:
            self.dp[N][sum]= self.isSubsetSum(N-1,arr,sum)
            return self.dp[N][sum]
