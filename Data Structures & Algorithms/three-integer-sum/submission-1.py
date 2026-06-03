class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()  # 排序是去重的大前提
        n = len(nums)
        
        for i in range(n):
            # 🚨 优化拦截 1：如果当前数字大于 0，因为数组是升序的，后面肯定都大于 0
            # 三个正数加起来绝对不可能等于 0，直接提前收工
            if nums[i] > 0:
                break
                
            # 🚨 核心去重 1：如果和前一个数字相同，说明这一轮是重复劳动，直接跳过
            # 注意：必须是 i > 0，因为 i = 0 时没有前一个数字
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = 0 - nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 🚨 核心去重 2：命中答案后，双指针在收缩时，必须跳过所有重复的值
                    # 比如当前 left 是 2，下一个也是 2，就一直往右推，直到看到不一样的数
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 同理，如果右边下一个数和当前一样，就一直往左推
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 别忘了！跳过重复值后，指针还要再各自迈进一格，走到全新的数字上
                    left += 1
                    right -= 1

                elif current_sum > target:
                    right -= 1
                else:
                    left += 1

        return result