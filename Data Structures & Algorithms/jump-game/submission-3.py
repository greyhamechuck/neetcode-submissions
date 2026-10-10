class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        if n == 1:
            return True
        maxj = 0
        for i in range(n):
            jump = nums[i]
            nxt = i+jump
            if maxj < i:
                return False
            maxj = max(maxj,nxt)
            if maxj >= n-1:
                return True
        return False