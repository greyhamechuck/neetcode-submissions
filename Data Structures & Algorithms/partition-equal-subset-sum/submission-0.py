class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        n= len(nums)
        if totalsum%2 !=0:
            return False
        
        middle = totalsum//2
        dp = [False] * (middle+1)
        dp[0] = True
        for num in nums:
            for j in range(middle,num-1,-1):
                dp[j] = dp[j-num] or dp[j]

        return dp[middle]