class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # 内置 DFS，不仅带着节点，还带着这个节点必须遵守的数学边界 [low, high]
        def dfs(node, low, high):
            # 边界门神：空树天然是合法的 BST
            if not node:
                return True
                
            # 核心判定：只要当前节点的值没有乖乖呆在 (low, high) 的开区间里，直接抓捕！
            if node.val <= low or node.val >= high:
                return False
                
            # 完美放行，分发任务给左右子树：
            # 1. 往左走：上界被锁死为当前 node.val
            left_valid = dfs(node.left, low, node.val)
            # 2. 往右走：下界被锁死为当前 node.val
            right_valid = dfs(node.right, node.val, high)
            
            # 只有左边合法 且 右边也合法，整棵树才算真正的 BST
            return left_valid and right_valid

        # 初始状态，根节点没有任何束缚，上下界给正负无穷大
        return dfs(root, float('-inf'), float('inf'))