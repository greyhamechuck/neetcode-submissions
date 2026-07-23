class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        lib = set(nums)

        for num in lib:
            if num-1 not in lib:
                curr = num
                count = 1
                while curr+1 in lib:
                    count +=1
                    curr +=1
            
                result = max(result,count)
        
        return result