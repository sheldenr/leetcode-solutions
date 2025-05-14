class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_map = {}
        row_map = {}
        col_map = {}

        for i in range(9): # Row
            for j in range(9): # Element

                # Add rows to row hashmap
                if row_map.get(i) == None:
                    if board[i][j].isalnum():
                        row_map[i] = [board[i][j]]
                else:
                    if board[i][j].isalnum():
                        row_map[i].append(board[i][j])

                # Add cols to col hashmap
                if col_map.get(j) == None:
                    if board[i][j].isalnum():
                        col_map[j] = [board[i][j]]
                else:
                    if board[i][j].isalnum():
                        col_map[j].append(board[i][j])

                # Add to proper box hashmap
                key = str(i // 3) + str(j // 3)
                if box_map.get(key) == None:
                    if board[i][j].isalnum():
                        box_map[key] = [board[i][j]]
                else:
                    if board[i][j].isalnum():
                        box_map[key].append(board[i][j])

        # Check if each box is clear of repetition
        for box_values in box_map.values():
            if len(box_values) != len(set(box_values)):
                return False

        # Check if row is clear of repetition
        for row_values in row_map.values():
            if len(row_values) != len(set(row_values)):
                return False
        
        # Check if row is clear of repetition
        for col_values in col_map.values():
            if len(col_values) != len(set(col_values)):
                return False

        return True
