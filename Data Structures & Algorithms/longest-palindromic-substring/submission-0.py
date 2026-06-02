class Solution:
    def longestPalindrome(self, s: str) -> str:
        recorder = ""
        count = 0
        length = len(s)
        def expander(left:int,right:int):
            while left >=0 and right < length and s[left] == s[right]:
                left -= 1
                right +=1
            return right-left-1

        for i in range(length):
            distance1 = expander(i,i)
            distance2= expander(i,i+1)
            distance = max(distance1,distance2)
            start = i - (distance - 1)//2
            end = i +(distance//2)
            if distance > count:
                recorder = s[start:end+1]
            count = max(distance,count)

        return recorder