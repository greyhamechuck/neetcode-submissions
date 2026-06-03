class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            target = 0 - nums[i]
            left = i+1
            right = n-1

            while left < right:
                if nums[left] + nums[right] == target:
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right -=1

                elif nums[left] + nums[right]> target:
                    right -= 1

                elif nums[left] + nums[right]<target:
                    left +=1


        return list(result)
