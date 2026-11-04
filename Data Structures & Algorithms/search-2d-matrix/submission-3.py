class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        length = len(matrix[0])-1
        left = 0
        right = n-1
        while left<=right:
            mid = (right-left)//2 + left

            if matrix[mid][0] <= target <=matrix[mid][length]:
                if target in matrix[mid]:
                    return True
                else:
                    return False

            elif target<matrix[mid][0]:
                right = mid-1

            else:
                left= mid+1

        
        return False