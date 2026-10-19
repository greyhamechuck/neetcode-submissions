class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)

        right = n-1
        result = 0
        while left<right:
            container = (right-left) * min(heights[left],heights[right])
            result = max(container,result)
            if heights[right]-heights[left]>0:
                left+=1
            else:
                right-=1

        
        return result
