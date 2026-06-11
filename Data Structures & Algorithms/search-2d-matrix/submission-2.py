class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lines = len(matrix)
        row = len(matrix[0])
        left = 0
        right = lines -1
        while left <= right:
            mid = (right-left)//2+left
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            elif target < matrix[mid][0]:
                right = mid-1
            else:
                left = mid +1
        return False