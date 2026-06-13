# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        def gethigh(root):
            if not root:
                return 0
            
            leftD = gethigh(root.left)
            rightD = gethigh(root.right)

            self.dia = max(leftD+rightD, self.dia)
            return max(leftD,rightD)+1
        gethigh(root)
        return self.dia