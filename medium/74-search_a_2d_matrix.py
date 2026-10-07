class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + (r - l) // 2)
            
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
                return True

            elif matrix[mid // len(matrix[0])][mid % len(matrix[0])] > target:
                r = (mid - 1)

            else:
                l = (mid + 1)

        return False
