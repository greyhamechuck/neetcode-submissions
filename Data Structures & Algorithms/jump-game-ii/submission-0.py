class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = 0
        max_end =0
        current = 0

        for i in range(n-1):
            max_end = max(i+nums[i],max_end)
            if i == current:
                step+=1
                current = max_end
                if current >= n - 1:
                    break

        return step
