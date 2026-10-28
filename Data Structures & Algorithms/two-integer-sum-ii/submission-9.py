class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        while left<right:
            ko = numbers[left] + numbers[right]
            if ko == target:
                return [left+1,right+1]

            if ko > target:
                right-=1

            elif ko < target:
                left+=1

        return 