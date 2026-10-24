class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                find= seen[target - nums[i]]
                return [find,i]
            seen[nums[i]] = i
        return []