class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right = len(height)-1
        leftmost = rightmost =0
        result = 0
        while left<=right:
            if height[right]>=rightmost:
                rightmost = height[right]
                right -= 1
            
            elif height[left] >= leftmost:
                leftmost = height[left]
                left+=1
            
            else:
                if leftmost < rightmost:
                    result += leftmost - height[left]
                    left +=1
                else:
                    result += rightmost - height[right]
                    right -= 1
        return result