class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmost=height[0]
        rightmost=height[n-1]
        left=0
        right=n-1
        result = 0
        while left<right:
            if leftmost<rightmost:
                left+=1
                leftmost = max(leftmost,height[left])
                result += leftmost - height[left]
            
            else:
                right-=1
                rightmost = max(rightmost,height[right])
                result += rightmost-height[right]

        return result
                