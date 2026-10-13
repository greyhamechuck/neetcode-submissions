class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left = 0
        right = length - 1
        
        while left < right:
            result = numbers[left] + numbers[right]

            if result < target:
                left +=1
            elif result > target:
                right -=1
            else:
                return [ left+1, right+1]

         