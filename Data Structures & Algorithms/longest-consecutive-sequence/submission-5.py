class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = 0
        hashset = set(nums)

        for num in nums:
            if num-1 not in hashset:
                curr = num
                count = 1
                while curr+1 in hashset:
                    curr +=1
                    count +=1
                
                total = max(total,count)
        
        return total