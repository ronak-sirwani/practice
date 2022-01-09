def partition(self,nums,n,target):
        if target==0:
            return True
        if n==0:
            return False
        
        if self.dp[n][target] !=-1:
            return self.dp[n][target]
        
        if nums[n-1] <= target:
            self.dp[n][target]= self.partition(nums,n-1,target-nums[n-1]) or self.partition(nums,n-1,target)
            return self.dp[n][target]
        else:
            self.dp[n][target]= self.partition(nums,n-1,target)
            return self.dp[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        n= len(nums)
        s= sum(nums)
        if s%2!=0:
            return False
        else:
            self.dp= [[-1 for i in range(s//2 + 1)] for j in range(n+1)]
            if self.partition(nums,n,s//2) :
                return True
            else:
                return False