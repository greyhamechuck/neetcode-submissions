# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        current = [(p,q)]

        while current:
            nextlevel = []

            for nodep, nodeq in current:
                if not nodep and not nodeq:
                    continue
                
                if not nodep or not nodeq or nodep.val != nodeq.val:
                    return False


                nextlevel.append((nodep.left, nodeq.left))
                nextlevel.append((nodep.right, nodeq.right))
            current = nextlevel
        return True