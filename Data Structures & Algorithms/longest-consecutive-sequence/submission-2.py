class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = 0
        length = len(nums)
        hashset = set(nums)
        for num in hashset:
            if num - 1 not in hashset:
                curr = num
                current_result = 1
                while (curr+1) in hashset:
                    current_result +=1
                    curr +=1

                total = max(current_result, total)

        return total