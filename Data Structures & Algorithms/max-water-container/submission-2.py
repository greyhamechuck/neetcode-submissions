class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left =0
        right = length-1
        cont = 0
        big = 0
        while left< right:
            cont = (right-left) * (min(heights[left],heights[right]))
            big = max(big,cont)
            if heights[left] < heights[right]:
                    left+=1
            else:
                    right-=1
                    
        return big