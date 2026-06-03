class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsub = minsub = nums[0]
        globalmax = nums[0]

        for i in range(1,len(nums)):

            maxsub,minsub = (
                max(nums[i],nums[i]*minsub,nums[i]*maxsub),
                min(nums[i],nums[i]*minsub,nums[i]*maxsub)
                )
            globalmax = max(maxsub,globalmax)


        return globalmax