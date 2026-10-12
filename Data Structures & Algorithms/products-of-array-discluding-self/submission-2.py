class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result1 = [1] * n
        prefix = 1
        for i in range(n):
            result1[i] =  prefix 
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            result1[i] *= suffix
            suffix *= nums[i]

        return result1