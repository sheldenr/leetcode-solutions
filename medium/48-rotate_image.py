class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # A 90 degrees rotation is equivalent to a transpose and a reflection across each row
        
        # Transpose
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflection
        for row in matrix:
            row.reverse()
        
