# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        current = [root]
        result = []
        if not root:
            return []
        
        while current:
            result.append(node.val for node in current)    
            next_level = []
            
            for node in current:
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            current = next_level
        
        return result