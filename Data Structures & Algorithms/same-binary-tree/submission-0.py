# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 初始把两个根节点当成“第一对战友”打包放进当前层
        current_level = [(p, q)]
        
        while current_level:
            next_level = []
            
            # 横向扫荡当前层的所有“节点对”
            for node_p, node_q in current_level:
                # 情况一：两个都是 None，安全，不用往下看了，直接跳过
                if not node_p and not node_q:
                    continue
                
                # 情况二：一个有一空，或者数字对不上，内鬼现身，直接返回 False
                if not node_p or not node_q or node_p.val != node_q.val:
                    return False
                
                # 情况三：当前这一对完全一样！安全过关。
                # 把它们各自的左儿子配成对、右儿子配成对，塞进下一层
                next_level.append((node_p.left, node_q.left))
                next_level.append((node_p.right, node_q.right))
            
            # 世代交替，滚动向前
            current_level = next_level
            
        return True