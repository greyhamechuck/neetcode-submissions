class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        left_most = heights[0] #1
        right_most = heights[-1] #6
        maxarea = (right-left) * min(heights[right],heights[left])

        while left < right:
            curr =  (right-left) * min(heights[right],heights[left])
            maxarea = max(curr,maxarea)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        

        return maxarea