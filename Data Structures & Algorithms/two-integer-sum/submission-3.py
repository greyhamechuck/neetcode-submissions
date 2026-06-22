class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            num = nums[i]
            comp = target - num
            if comp in seen:
                return [seen[comp],i]
            seen[num] = i
        
        return []
