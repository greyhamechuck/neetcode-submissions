class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length

        prefix = 1
        for i in range(length):
            result[i]  = prefix
            prefix *= nums[i]

        back = 1
        for i in range(length-1,-1,-1):
            result[i] *= back
            back*= nums[i]

        return result