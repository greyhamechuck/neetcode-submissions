class Solution:
    def isPalindrome(self, s: str) -> bool:
        kar = ""
        for ch in s:
            if ch.isalnum():
                kar += ch.lower()
        
        length = len(kar)
        return (kar == kar[::-1])