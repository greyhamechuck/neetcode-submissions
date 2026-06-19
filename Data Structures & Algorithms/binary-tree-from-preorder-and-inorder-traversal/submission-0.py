# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            val = inorder[i]
            inorder_map[val] = i

        def build(preL,preR,inoL,inoR):
            if preL> preR:
                return None
            
            rootval = preorder[preL]
            root = TreeNode(rootval)

            root_index = inorder_map[rootval]
            sizeleft = root_index - inoL
            root.left = build(preL+1,preL+sizeleft,inoL,root_index-1)
            root.right = build(preL+sizeleft+1,preR,root_index+1,inoR)
            return root
        n=len(preorder)
        return build(0,n-1,0,n-1)