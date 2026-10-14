class Solution:
    def trap(self, height: List[int]) -> int:
        maxarea = 0
        left=0
        right=len(height)-1
        leftmost=height[0]
        rightmost=height[right]
        while left < right:
                    if leftmost < rightmost:
                        left += 1
                        leftmost = max(leftmost, height[left])
                        maxarea += leftmost - height[left]
                    else:
                        right -= 1
                        rightmost = max(rightmost, height[right])
                        maxarea += rightmost - height[right]
                        
        return maxarea