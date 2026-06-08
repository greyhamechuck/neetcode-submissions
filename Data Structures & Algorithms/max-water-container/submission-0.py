class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = 0
        right = length -1
        initial = min(heights[0],heights[length-1]) * (length -1) 
        result = initial
        while left < right:
            distance = right - left
            current = min(heights[left],heights[right]) * distance 
            result = max(result, current)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        
        return result
