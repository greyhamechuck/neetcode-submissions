class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        # prev2 代表 dp[i-2] (初始为第 0 间房的最大值)
        # prev1 代表 dp[i-1] (初始为前两间房的最大值)
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        # 从第 2 间房（索引 2）开始遍历
        for i in range(2, len(nums)):
            # 状态转移方程
            current = max(prev1, prev2 + nums[i])
            # 滚动更新
            prev2 = prev1
            prev1 = current
            
        return prev1