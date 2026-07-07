class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())        
        n = len(s)
        middle = n//2
        for i in range(middle):
            if s[n-1-i] == s[i]:
                continue
            else:
                return False
        
        return True
