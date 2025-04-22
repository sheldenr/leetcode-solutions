class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_col = set()
        zero_row = set()

        # Traverse array to find zero columns and rows
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_col.add(col)
                    zero_row.add(row)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row in zero_row) or (col in zero_col):
                    matrix[row][col] = 0
            
        
