class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            haha = target - num

            if haha in seen:
                return [seen[haha],i]

            else:
                seen[num] = i