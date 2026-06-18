# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxn):
            if not node:
                return 0
            
            current = 0
            if node.val >= maxn:
                current += 1
                maxn = max(node.val,maxn)

            leftgood = dfs(node.left,maxn)
            rightgood = dfs(node.right,maxn)

            return leftgood+rightgood+current
        
        return dfs(root,root.val)