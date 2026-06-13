# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        currentlevel = [root]
        while currentlevel:
            nextlevel = [
            ]
            for node in currentlevel:
                node.left, node.right = node.right, node.left
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            currentlevel = nextlevel
        
        return root
            

