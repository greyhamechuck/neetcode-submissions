class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                
                if board[i][j] == ".":
                    continue

                col = (value,j)
                row = (i,value)
                circle = (i//3,j//3,value)

                if col in seen or row in seen or circle in seen:
                    return False
                
                seen.add(row)
                seen.add(col)
                seen.add(circle)

        return True
