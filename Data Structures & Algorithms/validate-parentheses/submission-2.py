class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                head = stack.pop() if stack else "#"

                if head != mapping.get(char):
                    return False

            else:
                stack.append(char)

        
        return len(stack) == 0