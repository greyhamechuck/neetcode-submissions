class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        nums.sort()
        counter = 1
        result = 1
        for i in range(l-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i+1] - nums[i]==1:
                counter +=1
            else:
                result = max(result,counter)
                counter = 1
        
        result = max(result,counter)
        return result