class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        result = 0
        def dfs(i,j):
            if i<0 or j<0 or i>= n or j >=m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return (
            1+            
            dfs(i+1,j)+
            dfs(i-1,j)+
            dfs(i,j-1)+
            dfs(i,j+1)
)

        for i in range(n):
            for j in range(m):
                if grid[i][j]== 1:
                    num = dfs(i,j)
                    result = max(result,num)

        return result